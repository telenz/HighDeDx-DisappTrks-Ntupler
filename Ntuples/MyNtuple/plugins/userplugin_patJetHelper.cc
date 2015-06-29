// ----------------------------------------------------------------------------
// Created: Mon Jun 29 17:26:51 2015 by mkhelper.py
// Author:  Teresa Lenz      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "Ntuples/MyNtuple/interface/patJetHelper.h"
typedef UserBuffer<pat::Jet, pat::JetHelper, COLLECTION>
patJetHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, patJetHelper_t,
                  "patJetHelper");
