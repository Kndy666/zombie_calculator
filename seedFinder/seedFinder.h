#pragma once

using namespace std;

class seedCalc
{
public:
	int currentProcess = 0;
	bool stopThread = false;
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