//
//--------------------------------------------------------------------
#include "Ntuples/MyNtuple/interface/recoTrackHelper.h"
#include "Ntuples/MyNtuple/interface/patElectronHelper.h"

namespace
{
  HelperFor<reco::Track> t_recoTrackHelper;
  HelperFor<pat::Electron> t_patElectronHelper;
}
