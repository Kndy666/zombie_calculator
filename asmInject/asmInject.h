#pragma once

#include "code.h"
#include "process.h"

class seedInject : public Code, public Process
{
public:
    enum class Result : int
    {
	    NotFound,
	    WrongVersion,
	    OpenError,
	    OK
    };

	seedInject();
	int getFrameDuration();
	void asm_code_inject();
	void setRandomSeed(int seed);
	int getRandomSeed();
	void internalSpawn();
	void updateZombiesType();
	void updateZombiesList();
	void updateZombiesPreview();
	Result findPvz();
private:
	void* extra_code_addr;
public:
	Result findResult;
};