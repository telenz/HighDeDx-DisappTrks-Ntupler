//
//--------------------------------------------------------------------
#include "Ntuples/MyNtuple/interface/recoTrackHelper.h"
#include "Ntuples/MyNtuple/interface/patElectronHelper.h"
#include "Ntuples/MyNtuple/interface/patJetHelper.h"
#include "Ntuples/MyNtuple/interface/edmEventHelperExtra.h"


namespace
{
  HelperFor<reco::Track> t_recoTrackHelper;
  HelperFor<pat::Electron> t_patElectronHelper;
  HelperFor<pat::Jet> t_patJetHelper;
  HelperFor<edm::Event> t_edmEventHelperExtra;
}
