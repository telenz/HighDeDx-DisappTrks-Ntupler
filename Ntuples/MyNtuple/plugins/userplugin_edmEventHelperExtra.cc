// ----------------------------------------------------------------------------
// Created: Mon Jun 29 19:01:41 2015 by mkhelper.py
// Author:  Teresa Lenz      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "Ntuples/MyNtuple/interface/edmEventHelperExtra.h"
typedef UserBuffer<edm::Event, edm::EventHelperExtra, SINGLETON>
edmEventHelperExtra_t;
DEFINE_EDM_PLUGIN(BufferFactory, edmEventHelperExtra_t,
                  "edmEventHelperExtra");
