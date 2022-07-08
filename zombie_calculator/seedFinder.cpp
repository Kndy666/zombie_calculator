#include <vector>
#include <array>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <random>
#include <thread>
#include <mutex>

using namespace std;
namespace py = pybind11;

inline array<int, 34> appear(int uid, int mode, const string& scene, int level, int seed)
{
	array<int, 34> havez{};
	for (int i = 0; i < havez.size(); ++i)havez[i] = 0;

	havez[0] = true;
	if (level == 0)
	{
		havez[2] = true;
		havez[4] = true;
	}
	else
	{
		int rd = uid + mode + 0x65 * level + seed;
		if (rd == 0x0)rd = 0x1105;
		mt19937 rng(rd);
		int rd1 = (rng() & 0x7FFFFFFF) % 5;
		if (rd1 == 0x0)havez[5] = true;
		else havez[2] = true;
		int typeRem = 9;
		if (level < 9)typeRem = level + 1;
		int typeHave = 0;
		while (typeHave < typeRem)
		{
			int rd2 = (rng() & 0x7FFFFFFF) % 33;
			if (havez[rd2])continue;
			else if (rd2 == 9 || rd2 == 10 || rd2 == 13 || rd2 == 19 || rd2 == 24 || (rd2 >= 26 && rd2 <= 31))continue;
			else if (scene == "NIGHT" && rd2 == 12)continue;
			else if ((scene != "POOL" && scene != "FOG") && (rd2 == 11 || rd2 == 14))continue;
			else if ((scene == "ROOF" || scene == "MOON") && (rd2 == 8 || rd2 == 17))continue;
			else if ((level < 2) && (rd2 == 12 || rd2 == 23))continue;
			else if ((level < 5) && (rd2 == 32))continue;
			else
			{
				havez[rd2] = true;
				typeHave++;
			}
		}
		havez[1] = false;
		havez[25] = false;
	}
	return havez;
}

class seedCalc
{
public:
	int currentProcess = 0;
	bool stopThread = false, overflow = false;
	int calc(const vector<vector<int> >& idNeeded, const vector<vector<int> >& idRefused);
	seedCalc(int uid, int mod, const string& scene, int level_beginning, int level_ending, int offset)
	{
		this->uid = uid;
		this->level_beginning = level_beginning;
		this->level_ending = level_ending;
		this->mod = mod;
		this->offset = offset;
		this->scene = scene;
	}
private:
	void calcThread(int startSeed, int step, int code);
	int uid, mod, level_ending, offset, level_beginning, res = 0;
	string scene;
	vector<vector<int> > idNeeded;
	vector<vector<int> > idRefused;
	mutex mtx;
};

void seedCalc::calcThread(int step, int startSeed, int code)
{
	int seed = startSeed;
	while (!res && !stopThread && !overflow)
	{
		bool fullFilled = false, aim1, aim2;
		for (int lvl = level_beginning; lvl < level_ending; ++lvl)
		{
			array<int, 34> zombies = appear(uid, mod, scene, lvl, seed);

			vector<int> eachWaveNeeded = idNeeded[lvl - 1];
			bool isBreakNeeded = false;
			for (int i = 0; i < eachWaveNeeded.size(); ++i)
			{
				int index = eachWaveNeeded[i];
				if (!zombies[index])
				{
					aim1 = false;
					isBreakNeeded = true;
					break;
				}
			}
			if (!isBreakNeeded)aim1 = true;
			if (!aim1)
			{
				seed += step;
				fullFilled = true;
				break;
			}

			vector<int> eachWaveRefused = idRefused[lvl - 1];
			bool isBreakRefused = false;
			for (int i = 0; i < eachWaveRefused.size(); ++i)
			{
				int index = eachWaveRefused[i];
				if (zombies[index])
				{
					aim2 = false;
					isBreakRefused = true;
					break;
				}
			}
			if (!isBreakRefused)aim2 = true;
			if (!aim2)
			{
				seed += step;
				fullFilled = true;
				break;
			}
		}
		if (!fullFilled)
		{
			mtx.lock();
			if (!res)res = seed;
			mtx.unlock();
			break;
		}
		if (!code)currentProcess = seed;
		if (seed < 0)overflow = true;
	}
}

int seedCalc::calc(const vector<vector<int> >& idNeeded, const vector<vector<int> >& idRefused)
{
	this->idNeeded = idNeeded;
	this->idRefused = idRefused;

	py::gil_scoped_release release;
	int num = thread::hardware_concurrency();
	vector<thread> threadList;
	for (int i = 0; i < num; ++i)
	{
		threadList.push_back(thread(&seedCalc::calcThread, this, num, i + offset, i));
	}
	for (int i = 0; i < num; ++i)
	{
		threadList[i].join();
	}
	py::gil_scoped_acquire acquire;
	return res;
}

PYBIND11_MODULE(seedFinder, m)
{
	m.doc() = "A module used to calculate pvz seed.";
	py::class_<seedCalc>(m, "requestToSeed")
		.def(py::init<int, int, const string&, int, int, int>())
		.def("calc", &seedCalc::calc, "start to calculate.")
		.def_readwrite("stopThread", &seedCalc::stopThread)
		.def_readwrite("overflow", &seedCalc::overflow)
		.def_readwrite("seed", &seedCalc::currentProcess);
	m.def("appear", &appear, "use seed to get a list with zombies id.",
		py::arg("uid"), py::arg("mode"), py::arg("scene"), py::arg("level"), py::arg("seed"));
}