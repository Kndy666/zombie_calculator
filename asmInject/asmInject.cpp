#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "asmInject.h"
#include "code.h"
#include "process.h"

namespace py = pybind11;

seedInject::seedInject()
{
    extra_code_addr = 0;
    findResult = this->findPvz();
}

int seedInject::getFrameDuration()
{
    int time_ms = 10;
    time_ms = ReadMemory<int>(0x6a9ec0, 0x454);
    return time_ms;
}

void seedInject::asm_code_inject()
{
    WriteMemory<byte>(0xfe, 0x00552014);
    Sleep(getFrameDuration() * 2);
    if (IsValid())
        Code::asm_code_inject(handle);
    WriteMemory<byte>(0xdb, 0x00552014);
}

void seedInject::setRandomSeed(int seed)
{
    WriteMemory<int>(seed, 0x6a9ec0, 0x768, 0x561c);
}

int seedInject::getRandomSeed()
{
    int seed = ReadMemory<int>(0x6a9ec0, 0x768, 0x561c);
    return seed;
}

void seedInject::internalSpawn()
{
    std::array<bool, 33> zombies = { false };
    WriteMemory(zombies, 0x6a9ec0, 0x768, 0x54d4);
    updateZombiesType();
    updateZombiesList();
    updateZombiesPreview();
}

void seedInject::updateZombiesList()
{
    asm_init();
    asm_mov_exx_dword_ptr(Reg::EDI, 0x6a9ec0);
    asm_mov_exx_dword_ptr_exx_add(Reg::EDI, 0x768);
    asm_call(0x004092e0);
    asm_ret();
    asm_code_inject();
}

void seedInject::updateZombiesPreview()
{
    WriteMemory<byte>(0x80, 0x0043a153);
    asm_init();
    asm_mov_exx_dword_ptr(Reg::EBX, 0x6a9ec0);
    asm_mov_exx_dword_ptr_exx_add(Reg::EBX, 0x768);
    asm_call(0x0040df70);
    asm_mov_exx_dword_ptr(Reg::EAX, 0x6a9ec0);
    asm_mov_exx_dword_ptr_exx_add(Reg::EAX, 0x768);
    asm_mov_exx_dword_ptr_exx_add(Reg::EAX, 0x15c);
    asm_push_exx(Reg::EAX);
    asm_call(0x0043a140);
    asm_ret();
    asm_code_inject();
    WriteMemory<byte>(0x85, 0x0043a153);
}

void seedInject::updateZombiesType()
{
    asm_init();
    asm_mov_exx_dword_ptr(Reg::ESI, 0x6a9ec0);
    asm_mov_exx_dword_ptr_exx_add(Reg::ESI, 0x768);
    asm_mov_exx_dword_ptr_exx_add(Reg::ESI, 0x160);
    asm_call(0x00425840);
    asm_ret();
    asm_code_inject();
}

seedInject::Result seedInject::findPvz()
{
    Result result;

    if (OpenByWindow(L"MainWindow", L"Plants vs. Zombies"))
        if (IsValid())
            if (ReadMemory<unsigned int>(0x004140c5) == 0x0019b337)
                result = Result::OK;
            else
                result = Result::WrongVersion;
        else
            result = Result::OpenError;
    else if (OpenByWindow(L"MainWindow", nullptr))
        if (IsValid())
            if (ReadMemory<unsigned int>(0x004140c5) == 0x0019b337)
                result = Result::OK;
            else
                result = Result::WrongVersion;
        else
            result = Result::OpenError;
    else
        result = Result::NotFound;
    return result;
}

PYBIND11_MODULE(asmInject, m)
{
    m.doc() = "A module uesd to inject asm code into pvz and read/write memory.";
    py::class_<seedInject> seedInjectInstance(m, "seedInject");
    seedInjectInstance.def(py::init<>())
        .def("setRandomSeed", &seedInject::setRandomSeed, "setSpawnSeed")
        .def("getRandomSeed", &seedInject::getRandomSeed, "getSpawnSeed")
        .def("internalSpawn", &seedInject::internalSpawn, "updateZombiesPreview")
        .def("findGame", 
            [](seedInject &injecter) {injecter.findResult = injecter.findPvz();})
        .def_readonly("findResult", &seedInject::findResult);
    py::enum_<seedInject::Result>(seedInjectInstance, "Result")
        .value("NotFound", seedInject::Result::NotFound)
        .value("OK", seedInject::Result::OK)
        .value("OpenError", seedInject::Result::OpenError)
        .value("WrongVersion", seedInject::Result::WrongVersion)
        .export_values();
}