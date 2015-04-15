// ----------------------------------------------------------------------------
// Created: Wed Apr 15 16:15:07 2015 by mkhelper.py
// Author:  Teresa Lenz      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "Ntuples/MyNtuple/interface/patElectronHelper.h"
typedef UserBuffer<pat::Electron, pat::ElectronHelper, COLLECTION>
patElectronHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, patElectronHelper_t,
                  "patElectronHelper");
