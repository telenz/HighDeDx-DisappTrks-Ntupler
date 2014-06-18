// ----------------------------------------------------------------------------
// Created: Wed Jun 18 15:59:24 2014 by mkhelper.py
// Author:  Teresa Lenz      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "Ntuples/MyNtuple/interface/recoTrackHelper.h"
typedef UserBuffer<reco::Track, reco::TrackHelper, COLLECTION>
recoTrackHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, recoTrackHelper_t,
                  "recoTrackHelper");
