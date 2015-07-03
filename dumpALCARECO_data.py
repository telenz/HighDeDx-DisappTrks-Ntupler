import FWCore.ParameterSet.Config as cms

process = cms.Process("ProtonAnalysis")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:ALCARECO.root')
)
process.CosmicMuonSeed = cms.EDProducer("CosmicMuonSeedGenerator",
    DTRecSegmentLabel = cms.InputTag("dt4DCosmicSegments"),
    CSCRecSegmentLabel = cms.InputTag("cscSegments"),
    EnableDTMeasurement = cms.bool(True),
    MaxCSCChi2 = cms.double(300.0),
    MaxDTChi2 = cms.double(300.0),
    MaxSeeds = cms.int32(1000),
    EnableCSCMeasurement = cms.bool(True)
)


process.MTMuons = cms.EDProducer("MuonIdProducer",
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("generalTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    maxAbsEta = cms.double(3.0),
    fillGlobalTrackRefits = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        ClusterDPhi = cms.double(0.6),
        OverlapDTheta = cms.double(0.02),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        ClusterDTheta = cms.double(0.02)
    ),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    addExtraSoftMuons = cms.bool(False),
    debugWithTruthMatching = cms.bool(False),
    CaloExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.2),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.5),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    ),
    runArbitrationCleaner = cms.bool(True),
    fillEnergy = cms.bool(False),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        usePosition = cms.bool(True),
        diagonalOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite')
    ),
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(6.0),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    inputCollectionTypes = cms.vstring('outer tracks'),
    minCaloCompatibility = cms.double(0.6),
    ecalDepositName = cms.string('ecal'),
    minP = cms.double(2.5),
    fillIsolation = cms.bool(False),
    jetDepositName = cms.string('jets'),
    hoDepositName = cms.string('ho'),
    writeIsoDeposits = cms.bool(True),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minPt = cms.double(0.5),
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    JetExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(0.5),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("ak5CaloJets"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    ),
    fillGlobalTrackQuality = cms.bool(True),
    minPCaloMuon = cms.double(1.0),
    maxAbsDy = cms.double(9999.0),
    fillCaloCompatibility = cms.bool(False),
    fillMatching = cms.bool(False),
    MuonCaloCompatibility = cms.PSet(
        allSiPMHO = cms.bool(False),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    fillTrackerKink = cms.bool(True),
    hcalDepositName = cms.string('hcal'),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    inputCollectionLabels = cms.VInputTag(cms.InputTag("MTSAMuons","UpdatedAtVtx")),
    trackDepositName = cms.string('tracker'),
    maxAbsDx = cms.double(3.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    minNumberOfMatches = cms.int32(1)
)


process.MTSAMuons = cms.EDProducer("StandAloneMuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    InputObjects = cms.InputTag("MTancientMuonSeed"),
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(True)
    ),
    STATrajBuilderParameters = cms.PSet(
        DoRefit = cms.bool(False),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            FitDirection = cms.string('insideOut'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
        NavigationType = cms.string('Standard'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            UseSubRecHits = cms.bool(False),
            NMinRecHits = cms.uint32(2),
            RescaleError = cms.double(100.0)
        ),
        DoBackwardFilter = cms.bool(True),
        SeedPosition = cms.string('in'),
        BWFilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            BWSeedType = cms.string('fromGenerator'),
            FitDirection = cms.string('outsideIn'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        RefitterParameters = cms.PSet(
            FitterName = cms.string('KFFitterSmootherSTA'),
            MaxFractionOfLostHits = cms.double(0.05),
            ForceAllIterations = cms.bool(False),
            NumberOfIterations = cms.uint32(3),
            RescaleError = cms.double(100.0)
        )
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive')
)


process.MTancientMuonSeed = cms.EDProducer("MuonSeedGenerator",
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    DTRecSegmentLabel = cms.InputTag("dt4DSegmentsMT"),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    EnableDTMeasurement = cms.bool(True),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    scaleDT = cms.bool(True),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, -0.0, 0.067, -0.001, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    crackWindow = cms.double(0.04),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    CSCRecSegmentLabel = cms.InputTag("cscSegments"),
    EnableCSCMeasurement = cms.bool(True),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0)
)


process.MTmuontiming = cms.EDProducer("MuonTimingProducer",
    MuonCollection = cms.InputTag("MTMuons"),
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegmentsMT"),
                DTradius = cms.double(1.0),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(3),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(False)
    )
)


process.MuonSeed = cms.EDProducer("MuonSeedProducer",
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, -0.0, 0.067, -0.001, 
        0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    minimumSeedPt = cms.double(5.0),
    minCSCHitsPerSegment = cms.int32(4),
    maxDeltaPhiDT = cms.double(0.3),
    defaultSeedPt = cms.double(25.0),
    EnableCSCMeasurement = cms.bool(True),
    maxDeltaPhiOverlap = cms.double(0.25),
    minDTHitsPerSegment = cms.int32(2),
    CSCSegmentLabel = cms.InputTag("cscSegments"),
    maxEtaResolutionCSC = cms.double(0.06),
    maxPhiResolutionCSC = cms.double(0.03),
    maxDeltaEtaOverlap = cms.double(0.08),
    EnableDTMeasurement = cms.bool(True),
    DTSegmentLabel = cms.InputTag("dt4DSegments"),
    SeedPtSystematics = cms.double(0.1),
    maximumSeedPt = cms.double(3000.0),
    maxEtaResolutionDT = cms.double(0.02),
    maxDeltaEtaCSC = cms.double(0.2),
    maxDeltaPhiCSC = cms.double(0.5),
    maxDeltaEtaDT = cms.double(0.3),
    DebugMuonSeed = cms.bool(False),
    maxPhiResolutionDT = cms.double(0.03)
)


process.MuonSegmentProducer = cms.EDProducer("MuonSegmentProducer",
    DTSegments = cms.InputTag("dt4DSegmentsMT"),
    CSCSegments = cms.InputTag("cscSegments")
)


process.RefitMTSAMuons = cms.EDProducer("StandAloneMuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    InputObjects = cms.InputTag("MTancientMuonSeed"),
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(True)
    ),
    STATrajBuilderParameters = cms.PSet(
        DoRefit = cms.bool(True),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            FitDirection = cms.string('insideOut'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
        NavigationType = cms.string('Standard'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            UseSubRecHits = cms.bool(False),
            NMinRecHits = cms.uint32(2),
            RescaleError = cms.double(100.0)
        ),
        DoBackwardFilter = cms.bool(True),
        SeedPosition = cms.string('in'),
        BWFilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            BWSeedType = cms.string('fromGenerator'),
            FitDirection = cms.string('outsideIn'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        RefitterParameters = cms.PSet(
            FitterName = cms.string('KFFitterSmootherSTA'),
            MaxFractionOfLostHits = cms.double(0.05),
            ForceAllIterations = cms.bool(False),
            NumberOfIterations = cms.uint32(3),
            RescaleError = cms.double(100.0)
        )
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive')
)


process.SETMuonSeed = cms.EDProducer("SETMuonSeedProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    SETTrajBuilderParameters = cms.PSet(
        SMB_21 = cms.vdouble(0.918425, -0.141199, 0.0, 0.254515, -0.111848, 
            0.0),
        SMB_20 = cms.vdouble(0.861314, -0.16233, 0.0, 0.248879, -0.113879, 
            0.0),
        SMB_22 = cms.vdouble(1.308565, -0.701634, 0.0, -0.302861, 0.675785, 
            0.0),
        OL_2213 = cms.vdouble(0.563218, -0.493991, 0.0, 0.943776, -0.591751, 
            0.0),
        SME_11 = cms.vdouble(2.39479, -0.888663, 0.0, -4.604546, 3.623464, 
            0.0),
        SME_13 = cms.vdouble(0.398851, 0.028176, 0.0, 0.567015, 2.623232, 
            0.0),
        SMB_31 = cms.vdouble(0.398661, -0.024853, 0.0, 0.863324, -0.413048, 
            0.0),
        SME_32 = cms.vdouble(-0.021912, -0.008995, 0.0, -49.779764, 30.780972, 
            0.0),
        SME_31 = cms.vdouble(-0.588188, 0.316961, 0.0, -95.261732, 45.444051, 
            0.0),
        OL_1213 = cms.vdouble(0.960544, -0.75644, 0.0, 0.1636, 0.114178, 
            0.0),
        DT_13 = cms.vdouble(0.298842, 0.076531, -0.14293, 0.219923, -0.145026, 
            0.155638),
        DT_12 = cms.vdouble(0.176182, 0.058535, -0.090549, 0.202363, -0.203126, 
            0.222219),
        DT_14 = cms.vdouble(0.388423, 0.068698, -0.145925, 0.159515, 0.124299, 
            -0.133269),
        OL_1232 = cms.vdouble(0.162626, 0.000843, 0.0, 0.396271, 0.002791, 
            0.0),
        CSC_23 = cms.vdouble(-0.095236, 0.122061, -0.029852, -11.396689, 15.933598, 
            -4.267065),
        CSC_24 = cms.vdouble(-0.049769, 0.063087, -0.011029, -13.765978, 16.296143, 
            -4.241835),
        CSC_03 = cms.vdouble(0.498992, -0.086235, -0.025772, 2.761006, -2.667607, 
            0.72802),
        CSC_01 = cms.vdouble(0.155906, -0.000406, 0.0, 0.194022, -0.010181, 
            0.0),
        SMB_32 = cms.vdouble(0.421649, -0.111654, 0.0, -0.044613, 1.134858, 
            0.0),
        SMB_30 = cms.vdouble(0.399628, 0.014922, 0.0, 0.665622, 0.358439, 
            0.0),
        OL_2222 = cms.vdouble(0.087587, 0.005729, 0.0, 0.535169, -0.087675, 
            0.0),
        SMB_10 = cms.vdouble(1.160532, 0.148991, 0.0, 0.182785, -0.093776, 
            0.0),
        SMB_11 = cms.vdouble(1.289468, -0.139653, 0.0, 0.137191, 0.01217, 
            0.0),
        SMB_12 = cms.vdouble(1.923091, -0.913204, 0.0, 0.161556, 0.020215, 
            0.0),
        DT_23 = cms.vdouble(0.120647, 0.034743, -0.070855, 0.302427, -0.21417, 
            0.261012),
        DT_24 = cms.vdouble(0.189527, 0.037328, -0.088523, 0.251936, 0.032411, 
            0.010984),
        SME_21 = cms.vdouble(0.64895, -0.148762, 0.0, -5.07676, 6.284227, 
            0.0),
        SME_22 = cms.vdouble(-0.624708, 0.641043, 0.0, 32.581295, -19.604264, 
            0.0),
        CSC_34 = cms.vdouble(0.144321, -0.142283, 0.035636, 190.260708, -180.888643, 
            43.430395),
        CSC_02 = cms.vdouble(0.600235, -0.205683, 0.001113, 0.655625, -0.682129, 
            0.253916),
        SME_42 = cms.vdouble(-0.021912, -0.008995, 0.0, -49.779764, 30.780972, 
            0.0),
        SME_41 = cms.vdouble(-0.187116, 0.076415, 0.0, -58.552583, 27.933864, 
            0.0),
        SME_12 = cms.vdouble(-0.277294, 0.7616, 0.0, -0.243326, 1.446792, 
            0.0),
        DT_34 = cms.vdouble(0.049146, -0.003494, -0.010099, 0.672095, 0.36459, 
            -0.304346),
        CSC_14 = cms.vdouble(0.952517, -0.532733, 0.084601, 1.615881, -1.630744, 
            0.514139),
        OL_1222 = cms.vdouble(0.215915, 0.002556, 0.0, 0.313596, -0.021465, 
            0.0),
        CSC_13 = cms.vdouble(1.22495, -1.792358, 0.711378, 5.271848, -6.280625, 
            2.0142),
        CSC_12 = cms.vdouble(-0.363549, 0.569552, -0.173186, 7.777069, -10.203618, 
            3.478874),
        DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
        DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
        CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
        SME_13_0_scale = cms.vdouble(0.104905, 0.0),
        SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
        DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
        OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
        OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
        SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
        DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
        CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
        OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
        CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
        OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
        SME_11_0_scale = cms.vdouble(1.325085, 0.0),
        CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
        SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
        SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
        DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
        SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
        CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
        DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
        SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
        CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
        CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
        DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
        SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
        DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
        SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
        SME_12_0_scale = cms.vdouble(2.279181, 0.0),
        CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
        DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
        SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
        SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
        SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
        DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
        CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
        DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
        DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
        CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
        CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
        OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
        scaleDT = cms.bool(True),
        Apply_prePruning = cms.bool(True),
        UseSegmentsInTrajectory = cms.bool(False),
        FilterParameters = cms.PSet(
            OutsideChamberErrorScale = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MinLocalSegmentAngle = cms.double(0.09),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            maxActiveChambers = cms.int32(100),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        )
    ),
    beamSpotTag = cms.InputTag("offlineBeamSpot")
)


process.TrackProducer = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.TrackRefitter = cms.EDProducer("TrackRefitter",
    src = cms.InputTag("generalTracksReduced"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    srcConstr = cms.InputTag(""),
    constraint = cms.string(''),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.TrackRefitterBHM = cms.EDProducer("TrackRefitter",
    src = cms.InputTag("ctfWithMaterialTracksBeamHaloMuon"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    srcConstr = cms.InputTag(""),
    constraint = cms.string(''),
    Fitter = cms.string('KFFittingSmootherBH'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('BeamHaloPropagatorAlong')
)


process.TrackRefitterP5 = cms.EDProducer("TrackRefitter",
    src = cms.InputTag("ctfWithMaterialTracksP5"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    srcConstr = cms.InputTag(""),
    constraint = cms.string(''),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ancientMuonSeed = cms.EDProducer("MuonSeedGenerator",
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, -0.0, 0.067, -0.001, 
        0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    crackWindow = cms.double(0.04),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    CSCRecSegmentLabel = cms.InputTag("cscSegments"),
    scaleDT = cms.bool(True),
    EnableDTMeasurement = cms.bool(True),
    DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
    EnableCSCMeasurement = cms.bool(True)
)


process.beamhaloTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("beamhaloTrackerSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('BeamHaloPropagatorAlong'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('BeamHaloPropagatorOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('BeamHaloNavigationSchool'),
    TrajectoryBuilder = cms.string('CkfTrajectoryBuilderBH')
)


process.beamhaloTrackerSeeds = cms.EDProducer("CtfSpecialSeedGenerator",
    ErrorRescaling = cms.double(50.0),
    OrderedHitsFactoryPSets = cms.VPSet(cms.PSet(
        ComponentName = cms.string('BeamHaloPairGenerator'),
        maxTheta = cms.double(0.1),
        NavigationDirection = cms.string('outsideIn'),
        LayerPSet = cms.PSet(
            TEC4 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC5 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC6 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC = cms.PSet(
                minRing = cms.int32(5),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(7)
            ),
            TEC1 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC2 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC3 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            FPix = cms.PSet(
                hitErrorRZ = cms.double(0.0036),
                hitErrorRPhi = cms.double(0.0051),
                TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
                HitProducer = cms.string('siPixelRecHits'),
                useErrorsFromParam = cms.bool(True)
            ),
            TID = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            layerList = cms.vstring('FPix1_pos+FPix2_pos', 
                'FPix1_neg+FPix2_neg', 
                'TID2_pos+TID3_pos', 
                'TID2_neg+TID3_neg', 
                'TEC1_neg+TEC2_neg', 
                'TEC1_pos+TEC2_pos', 
                'TEC2_neg+TEC3_neg', 
                'TEC2_pos+TEC3_pos', 
                'TEC3_neg+TEC4_neg', 
                'TEC3_pos+TEC4_pos', 
                'TEC4_neg+TEC5_neg', 
                'TEC4_pos+TEC5_pos', 
                'TEC5_neg+TEC6_neg', 
                'TEC5_pos+TEC6_pos', 
                'TEC7_neg+TEC8_neg', 
                'TEC7_pos+TEC8_pos', 
                'TEC8_neg+TEC9_neg', 
                'TEC8_pos+TEC9_pos')
        ),
        PropagationDirection = cms.string('alongMomentum')
    ), 
        cms.PSet(
            ComponentName = cms.string('BeamHaloPairGenerator'),
            maxTheta = cms.double(0.1),
            NavigationDirection = cms.string('outsideIn'),
            LayerPSet = cms.PSet(
                TEC4 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC5 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC6 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                ),
                TEC1 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC2 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC3 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                FPix = cms.PSet(
                    hitErrorRZ = cms.double(0.0036),
                    hitErrorRPhi = cms.double(0.0051),
                    TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
                    HitProducer = cms.string('siPixelRecHits'),
                    useErrorsFromParam = cms.bool(True)
                ),
                TID = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                layerList = cms.vstring('FPix1_pos+FPix2_pos', 
                    'FPix1_neg+FPix2_neg', 
                    'TID2_pos+TID3_pos', 
                    'TID2_neg+TID3_neg', 
                    'TEC1_neg+TEC2_neg', 
                    'TEC1_pos+TEC2_pos', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_neg+TEC9_neg', 
                    'TEC8_pos+TEC9_pos')
            ),
            PropagationDirection = cms.string('oppositeToMomentum')
        )),
    Charges = cms.vint32(-1, 1),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(10000),
    UseScintillatorsConstraint = cms.bool(False),
    SetMomentum = cms.bool(True),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originHalfLength = cms.double(21.2),
            originZPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            ptMin = cms.double(0.9),
            originXPos = cms.double(0.0),
            originRadius = cms.double(0.2)
        ),
        ComponentName = cms.string('GlobalRegionProducer')
    ),
    SeedsFromNegativeY = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    SeedsFromPositiveY = cms.bool(False),
    MaxNumberOfPixelClusters = cms.uint32(10000),
    SeedMomentum = cms.double(15.0),
    maxSeeds = cms.int32(10000),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    requireBOFF = cms.bool(False)
)


process.beamhaloTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("beamhaloTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherBH'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('beamhaloTracks'),
    NavigationSchool = cms.string('BeamHaloNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('beamhalo'),
    Propagator = cms.string('BeamHaloPropagatorAlong')
)


process.calomuons = cms.EDProducer("CaloMuonProducer",
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    MuonCaloCompatibility = cms.PSet(
        allSiPMHO = cms.bool(False),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    inputMuons = cms.InputTag("muons1stStep"),
    inputTracks = cms.InputTag("generalTracks"),
    minCaloCompatibility = cms.double(0.6),
    inputCollection = cms.InputTag("muons1stStep"),
    minPt = cms.double(1.0)
)


process.ckfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalMixedSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder')
)


process.ckfTrackCandidatesCombinedSeeds = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalCombinedSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder')
)


process.ckfTrackCandidatesNoOverlaps = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalMixedSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('CkfTrajectoryBuilder')
)


process.ckfTrackCandidatesP5 = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("combinedP5SeedsForCTF"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilderP5')
)


process.ckfTrackCandidatesP5Bottom = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("combinedP5SeedsForCTFBottom"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilderP5Bottom')
)


process.ckfTrackCandidatesP5LHCNavigation = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("combinedP5SeedsForCTF"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilderP5')
)


process.ckfTrackCandidatesP5Top = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("combinedP5SeedsForCTFTop"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilderP5Top')
)


process.ckfTrackCandidatesPixelLess = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalPixelLessSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder')
)


process.combinatorialcosmicseedfinder = cms.EDProducer("CtfSpecialSeedGenerator",
    ErrorRescaling = cms.double(50.0),
    OrderedHitsFactoryPSets = cms.VPSet(cms.PSet(
        ComponentName = cms.string('GenericTripletGenerator'),
        LayerPSet = cms.PSet(
            TOB5 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TOB4 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TIB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB6 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TOB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TOB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TEC = cms.PSet(
                useSimpleRphiHitsCleaner = cms.bool(True),
                minRing = cms.int32(5),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(7)
            ),
            TIB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TIB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            layerList = cms.vstring('TOB4+TOB5+TOB6', 
                'TOB3+TOB5+TOB6', 
                'TOB3+TOB4+TOB5', 
                'TOB2+TOB4+TOB5', 
                'TOB3+TOB4+TOB6', 
                'TOB2+TOB4+TOB6')
        ),
        PropagationDirection = cms.string('alongMomentum'),
        NavigationDirection = cms.string('outsideIn')
    ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                TOB5 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB4 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TIB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB6 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TEC = cms.PSet(
                    useSimpleRphiHitsCleaner = cms.bool(True),
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                ),
                TIB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TIB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                layerList = cms.vstring('TEC1_pos+TEC2_pos', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC6_pos+TEC7_pos', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_pos+TEC9_pos')
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericTripletGenerator'),
            LayerPSet = cms.PSet(
                TOB5 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB4 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TIB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB6 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TEC = cms.PSet(
                    useSimpleRphiHitsCleaner = cms.bool(True),
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                ),
                TIB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TIB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                layerList = cms.vstring('TIB1+TIB2+TIB3')
            ),
            PropagationDirection = cms.string('oppositeToMomentum'),
            NavigationDirection = cms.string('insideOut')
        )),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    Charges = cms.vint32(-1),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    UseScintillatorsConstraint = cms.bool(True),
    SetMomentum = cms.bool(True),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originHalfLength = cms.double(21.2),
            originZPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            ptMin = cms.double(0.9),
            originXPos = cms.double(0.0),
            originRadius = cms.double(0.2)
        ),
        ComponentName = cms.string('GlobalRegionProducer')
    ),
    SeedsFromNegativeY = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    SeedsFromPositiveY = cms.bool(True),
    MaxNumberOfPixelClusters = cms.uint32(300),
    SeedMomentum = cms.double(5.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    maxSeeds = cms.int32(10000),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    requireBOFF = cms.bool(False)
)


process.combinatorialcosmicseedfinderP5 = cms.EDProducer("CtfSpecialSeedGenerator",
    ErrorRescaling = cms.double(50.0),
    OrderedHitsFactoryPSets = cms.VPSet(cms.PSet(
        ComponentName = cms.string('GenericTripletGenerator'),
        LayerPSet = cms.PSet(
            TOB5 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TOB4 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TIB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB6 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TOB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            TOB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TEC = cms.PSet(
                useSimpleRphiHitsCleaner = cms.bool(True),
                minRing = cms.int32(5),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(7)
            ),
            TIB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TIB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            layerList = cms.vstring('TOB4+TOB5+TOB6', 
                'TOB3+TOB5+TOB6', 
                'TOB3+TOB4+TOB5', 
                'TOB2+TOB4+TOB5', 
                'TOB3+TOB4+TOB6', 
                'TOB2+TOB4+TOB6')
        ),
        PropagationDirection = cms.string('alongMomentum'),
        NavigationDirection = cms.string('outsideIn')
    ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                TOB5 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB4 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TIB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB6 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                TOB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TEC = cms.PSet(
                    useSimpleRphiHitsCleaner = cms.bool(True),
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                ),
                TIB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TIB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                layerList = cms.vstring('TOB5+TOB6', 
                    'TOB4+TOB5')
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_pos+TEC2_pos', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC6_pos+TEC7_pos', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_pos+TEC9_pos'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_pos+TEC2_pos', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC6_pos+TEC7_pos', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_pos+TEC9_pos'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('insideOut')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_neg+TEC2_neg', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC6_neg+TEC7_neg', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC8_neg+TEC9_neg'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_neg+TEC2_neg', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC6_neg+TEC7_neg', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC8_neg+TEC9_neg'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('insideOut')
        )),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    Charges = cms.vint32(-1),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    UseScintillatorsConstraint = cms.bool(False),
    SetMomentum = cms.bool(True),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originHalfLength = cms.double(21.2),
            originZPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            ptMin = cms.double(0.9),
            originXPos = cms.double(0.0),
            originRadius = cms.double(0.2)
        ),
        ComponentName = cms.string('GlobalRegionProducer')
    ),
    SeedsFromNegativeY = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    SeedsFromPositiveY = cms.bool(True),
    MaxNumberOfPixelClusters = cms.uint32(300),
    SeedMomentum = cms.double(5.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    maxSeeds = cms.int32(10000),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    requireBOFF = cms.bool(True)
)


process.combinatorialcosmicseedfinderP5Bottom = cms.EDProducer("CtfSpecialSeedGenerator",
    ErrorRescaling = cms.double(50.0),
    OrderedHitsFactoryPSets = cms.VPSet(cms.PSet(
        ComponentName = cms.string('GenericTripletGenerator'),
        LayerPSet = cms.PSet(
            TOB5 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
            ),
            TOB4 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
            ),
            TIB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB6 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
            ),
            TOB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
            ),
            TOB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TEC = cms.PSet(
                useSimpleRphiHitsCleaner = cms.bool(True),
                minRing = cms.int32(5),
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
                maxRing = cms.int32(7)
            ),
            TIB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TIB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
            ),
            layerList = cms.vstring('TOB4+TOB5+TOB6', 
                'TOB3+TOB5+TOB6', 
                'TOB3+TOB4+TOB5', 
                'TOB2+TOB4+TOB5', 
                'TOB3+TOB4+TOB6', 
                'TOB2+TOB4+TOB6')
        ),
        PropagationDirection = cms.string('oppositeToMomentum'),
        NavigationDirection = cms.string('outsideIn')
    ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                TOB5 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
                ),
                TOB4 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
                ),
                TIB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB6 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
                ),
                TOB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
                ),
                TOB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TEC = cms.PSet(
                    useSimpleRphiHitsCleaner = cms.bool(True),
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
                    maxRing = cms.int32(7)
                ),
                TIB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TIB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
                ),
                layerList = cms.vstring('TOB5+TOB6', 
                    'TOB4+TOB5')
            ),
            PropagationDirection = cms.string('oppositeToMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_pos+TEC2_pos', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC6_pos+TEC7_pos', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_pos+TEC9_pos'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('oppositeToMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_pos+TEC2_pos', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC6_pos+TEC7_pos', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_pos+TEC9_pos'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('oppositeToMomentum'),
            NavigationDirection = cms.string('insideOut')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_neg+TEC2_neg', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC6_neg+TEC7_neg', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC8_neg+TEC9_neg'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('oppositeToMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_neg+TEC2_neg', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC6_neg+TEC7_neg', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC8_neg+TEC9_neg'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('oppositeToMomentum'),
            NavigationDirection = cms.string('insideOut')
        )),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    Charges = cms.vint32(-1),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    UseScintillatorsConstraint = cms.bool(False),
    SetMomentum = cms.bool(True),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originHalfLength = cms.double(21.2),
            originZPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            ptMin = cms.double(0.9),
            originXPos = cms.double(0.0),
            originRadius = cms.double(0.2)
        ),
        ComponentName = cms.string('GlobalRegionProducer')
    ),
    SeedsFromNegativeY = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    SeedsFromPositiveY = cms.bool(False),
    MaxNumberOfPixelClusters = cms.uint32(300),
    SeedMomentum = cms.double(5.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    maxSeeds = cms.int32(10000),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClustersBottom"),
    requireBOFF = cms.bool(True)
)


process.combinatorialcosmicseedfinderP5Top = cms.EDProducer("CtfSpecialSeedGenerator",
    ErrorRescaling = cms.double(50.0),
    OrderedHitsFactoryPSets = cms.VPSet(cms.PSet(
        ComponentName = cms.string('GenericTripletGenerator'),
        LayerPSet = cms.PSet(
            TOB5 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
            ),
            TOB4 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
            ),
            TIB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB6 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
            ),
            TOB1 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TOB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
            ),
            TOB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TEC = cms.PSet(
                useSimpleRphiHitsCleaner = cms.bool(True),
                minRing = cms.int32(5),
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
                maxRing = cms.int32(7)
            ),
            TIB2 = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TIB3 = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
            ),
            layerList = cms.vstring('TOB4+TOB5+TOB6', 
                'TOB3+TOB5+TOB6', 
                'TOB3+TOB4+TOB5', 
                'TOB2+TOB4+TOB5', 
                'TOB3+TOB4+TOB6', 
                'TOB2+TOB4+TOB6')
        ),
        PropagationDirection = cms.string('alongMomentum'),
        NavigationDirection = cms.string('outsideIn')
    ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                TOB5 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
                ),
                TOB4 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
                ),
                TIB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB6 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
                ),
                TOB1 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TOB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
                ),
                TOB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TEC = cms.PSet(
                    useSimpleRphiHitsCleaner = cms.bool(True),
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
                    maxRing = cms.int32(7)
                ),
                TIB2 = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    TTRHBuilder = cms.string('WithTrackAngle')
                ),
                TIB3 = cms.PSet(
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
                ),
                layerList = cms.vstring('TOB5+TOB6', 
                    'TOB4+TOB5')
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_pos+TEC2_pos', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC6_pos+TEC7_pos', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_pos+TEC9_pos'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_pos+TEC2_pos', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC6_pos+TEC7_pos', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_pos+TEC9_pos'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('insideOut')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_neg+TEC2_neg', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC6_neg+TEC7_neg', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC8_neg+TEC9_neg'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('outsideIn')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerPSet = cms.PSet(
                layerList = cms.vstring('TEC1_neg+TEC2_neg', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC6_neg+TEC7_neg', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC8_neg+TEC9_neg'),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
                    maxRing = cms.int32(7)
                )
            ),
            PropagationDirection = cms.string('alongMomentum'),
            NavigationDirection = cms.string('insideOut')
        )),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    Charges = cms.vint32(-1),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    UseScintillatorsConstraint = cms.bool(False),
    SetMomentum = cms.bool(True),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originHalfLength = cms.double(21.2),
            originZPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            ptMin = cms.double(0.9),
            originXPos = cms.double(0.0),
            originRadius = cms.double(0.2)
        ),
        ComponentName = cms.string('GlobalRegionProducer')
    ),
    SeedsFromNegativeY = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    SeedsFromPositiveY = cms.bool(True),
    MaxNumberOfPixelClusters = cms.uint32(300),
    SeedMomentum = cms.double(5.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        WidthInX = cms.double(100.0),
        LenghtInZ = cms.double(100.0)
    ),
    maxSeeds = cms.int32(10000),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClustersTop"),
    requireBOFF = cms.bool(True)
)


process.combinedP5SeedsForCTF = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("combinatorialcosmicseedfinderP5"), cms.InputTag("simpleCosmicBONSeeds")),
    PairCollection = cms.InputTag("combinatorialcosmicseedfinderP5"),
    TripletCollection = cms.InputTag("simpleCosmicBONSeeds")
)


process.combinedP5SeedsForCTFBottom = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("combinatorialcosmicseedfinderP5Bottom"), cms.InputTag("simpleCosmicBONSeedsBottom"))
)


process.combinedP5SeedsForCTFTop = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("combinatorialcosmicseedfinderP5Top"), cms.InputTag("simpleCosmicBONSeedsTop"))
)


process.convClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("tobTecStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("tobTecStepSelector","tobTecStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(30.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.convStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("convStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(1),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(3),
        chi2n_par = cms.double(3.0),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(5.0, 8.0),
        applyAdaptedPVCuts = cms.bool(False),
        dz_par1 = cms.vdouble(5.0, 8.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('convStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(5.0, 8.0),
        d0_par1 = cms.vdouble(5.0, 8.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(1),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(2.5),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('convStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('convStepLoose'),
            d0_par2 = cms.vdouble(5.0, 8.0),
            d0_par1 = cms.vdouble(5.0, 8.0),
            res_par = cms.vdouble(0.003, 0.001),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(1),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(2.0),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(5.0, 8.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('convStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(5.0, 8.0),
            d0_par1 = cms.vdouble(5.0, 8.0),
            preFilterName = cms.string('convStepTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.convStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("convTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('convStepFitterSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter8'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.convTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("photonConvTrajSeedFromSingleLeg","convSeedCandidates"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('convCkfTrajectoryBuilder')
)


process.conversionStepTracks = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(False),
    MinPT = cms.double(0.05),
    makeReKeyedSeeds = cms.untracked.bool(False),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("convStepSelector","convStep")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1),
    FoundHitBonus = cms.double(5.0),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(1)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("convStepTracks")),
    LostHitPenalty = cms.double(20.0),
    newQuality = cms.string('confirmed')
)


process.cosmicCandidateFinder = cms.EDProducer("CosmicTrackFinder",
    MinHits = cms.int32(4),
    HitProducer = cms.string('siStripRecHits'),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    useHitsSplitting = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    Chi2Cut = cms.double(30.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    debug = cms.untracked.bool(True),
    GeometricStructure = cms.untracked.string('MTCC'),
    cosmicSeeds = cms.InputTag("cosmicseedfinder")
)


process.cosmicCandidateFinderP5 = cms.EDProducer("CosmicTrackFinder",
    MinHits = cms.int32(4),
    HitProducer = cms.string('siStripRecHits'),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    useHitsSplitting = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    Chi2Cut = cms.double(30.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    debug = cms.untracked.bool(True),
    GeometricStructure = cms.untracked.string('STANDARD'),
    cosmicSeeds = cms.InputTag("cosmicseedfinderP5")
)


process.cosmicCandidateFinderP5Bottom = cms.EDProducer("CosmicTrackFinder",
    MinHits = cms.int32(4),
    HitProducer = cms.string('siStripRecHitsBottom'),
    pixelRecHits = cms.InputTag("siPixelRecHitsBottom"),
    useHitsSplitting = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit"),
    Chi2Cut = cms.double(30.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    debug = cms.untracked.bool(True),
    GeometricStructure = cms.untracked.string('STANDARD'),
    cosmicSeeds = cms.InputTag("cosmicseedfinderP5Bottom")
)


process.cosmicCandidateFinderP5Top = cms.EDProducer("CosmicTrackFinder",
    MinHits = cms.int32(4),
    HitProducer = cms.string('siStripRecHitsTop'),
    pixelRecHits = cms.InputTag("siPixelRecHitsTop"),
    useHitsSplitting = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    Chi2Cut = cms.double(30.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    debug = cms.untracked.bool(True),
    GeometricStructure = cms.untracked.string('STANDARD'),
    cosmicSeeds = cms.InputTag("cosmicseedfinderP5Top")
)


process.cosmicMuons = cms.EDProducer("CosmicMuonProducer",
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        PutTrajectoryIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False),
        AllowNoVertex = cms.untracked.bool(True),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrajectoryBuilderParameters = cms.PSet(
        BackwardMuonTrajectoryUpdatorParameters = cms.PSet(
            MaxChi2 = cms.double(100.0),
            RescaleErrorFactor = cms.double(1.0),
            Granularity = cms.int32(2),
            ExcludeRPCFromFit = cms.bool(True),
            UseInvalidHits = cms.bool(False),
            RescaleError = cms.bool(False)
        ),
        DTRecSegmentLabel = cms.InputTag("dt4DCosmicSegments"),
        MuonTrajectoryUpdatorParameters = cms.PSet(
            MaxChi2 = cms.double(3000.0),
            RescaleErrorFactor = cms.double(1.0),
            Granularity = cms.int32(0),
            ExcludeRPCFromFit = cms.bool(True),
            UseInvalidHits = cms.bool(False),
            RescaleError = cms.bool(False)
        ),
        EnableRPCMeasurement = cms.bool(True),
        CSCRecSegmentLabel = cms.InputTag("cscSegments"),
        BuildTraversingMuon = cms.bool(False),
        Strict1Leg = cms.bool(False),
        EnableDTMeasurement = cms.bool(True),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        MuonSmootherParameters = cms.PSet(
            PropagatorAlong = cms.string('SteppingHelixPropagatorAny'),
            PropagatorOpposite = cms.string('SteppingHelixPropagatorAny'),
            RescalingFactor = cms.double(5.0)
        ),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        EnableCSCMeasurement = cms.bool(True),
        MuonNavigationParameters = cms.PSet(
            Barrel = cms.bool(True),
            Endcap = cms.bool(True)
        )
    ),
    MuonSeedCollectionLabel = cms.string('CosmicMuonSeed')
)


process.cosmicMuons1Leg = cms.EDProducer("CosmicMuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrajectoryBuilderParameters = cms.PSet(
        BackwardMuonTrajectoryUpdatorParameters = cms.PSet(
            MaxChi2 = cms.double(100.0),
            RescaleErrorFactor = cms.double(1.0),
            Granularity = cms.int32(2),
            ExcludeRPCFromFit = cms.bool(True),
            UseInvalidHits = cms.bool(False),
            RescaleError = cms.bool(False)
        ),
        DTRecSegmentLabel = cms.InputTag("dt4DCosmicSegments"),
        MuonTrajectoryUpdatorParameters = cms.PSet(
            MaxChi2 = cms.double(3000.0),
            RescaleErrorFactor = cms.double(1.0),
            Granularity = cms.int32(0),
            ExcludeRPCFromFit = cms.bool(True),
            UseInvalidHits = cms.bool(False),
            RescaleError = cms.bool(False)
        ),
        EnableRPCMeasurement = cms.bool(True),
        CSCRecSegmentLabel = cms.InputTag("cscSegments"),
        BuildTraversingMuon = cms.bool(True),
        Strict1Leg = cms.bool(True),
        EnableDTMeasurement = cms.bool(True),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        MuonSmootherParameters = cms.PSet(
            PropagatorAlong = cms.string('SteppingHelixPropagatorAny'),
            PropagatorOpposite = cms.string('SteppingHelixPropagatorAny'),
            RescalingFactor = cms.double(5.0)
        ),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        EnableCSCMeasurement = cms.bool(True),
        MuonNavigationParameters = cms.PSet(
            Barrel = cms.bool(True),
            Endcap = cms.bool(True)
        )
    ),
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        PutTrajectoryIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False),
        AllowNoVertex = cms.untracked.bool(True),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False)
    ),
    MuonSeedCollectionLabel = cms.string('CosmicMuonSeed')
)


process.cosmicTrackSplitter = cms.EDProducer("CosmicTrackSplitter",
    dxyCut = cms.double(9999.0),
    stripBackInvalidHits = cms.bool(True),
    stripAllInvalidHits = cms.bool(False),
    tracks = cms.InputTag("cosmictrackfinderCosmics"),
    excludePixelHits = cms.bool(False),
    tjTkAssociationMapTag = cms.InputTag("cosmictrackfinderCosmics"),
    replaceWithInactiveHits = cms.bool(False),
    dzCut = cms.double(9999.0),
    minimumHits = cms.uint32(6),
    detsToIgnore = cms.vuint32(),
    stripFrontInvalidHits = cms.bool(True)
)


process.cosmicsVeto = cms.EDProducer("CosmicsMuonIdProducer",
    CosmicCompFillerParameters = cms.PSet(
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                'SteppingHelixPropagatorAlong', 
                'SteppingHelixPropagatorOpposite', 
                'SteppingHelixPropagatorL2Any', 
                'SteppingHelixPropagatorL2Along', 
                'SteppingHelixPropagatorL2Opposite', 
                'SteppingHelixPropagatorAnyNoError', 
                'SteppingHelixPropagatorAlongNoError', 
                'SteppingHelixPropagatorOppositeNoError', 
                'SteppingHelixPropagatorL2AnyNoError', 
                'SteppingHelixPropagatorL2AlongNoError', 
                'SteppingHelixPropagatorL2OppositeNoError', 
                'PropagatorWithMaterial', 
                'PropagatorWithMaterialOpposite', 
                'SmartPropagator', 
                'SmartPropagatorOpposite', 
                'SmartPropagatorAnyOpposite', 
                'SmartPropagatorAny', 
                'SmartPropagatorRK', 
                'SmartPropagatorAnyRK', 
                'StraightLinePropagator'),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        deltaPt = cms.double(0.1),
        maxdzTight = cms.double(10.0),
        offTimeNegTight = cms.double(-20.0),
        maxvertRho = cms.double(5),
        ipCut = cms.double(0.02),
        segmentComp = cms.double(0.4),
        sharedFrac = cms.double(0.75),
        angleCut = cms.double(0.1),
        hIpTrvProb = cms.double(0.5),
        InputMuonCollections = cms.VInputTag(cms.InputTag("globalMuons"), cms.InputTag("muons1stStep")),
        maxdxyTight = cms.double(1.0),
        maxdzLoose = cms.double(0.1),
        InputTrackCollections = cms.VInputTag(cms.InputTag("generalTracks"), cms.InputTag("cosmicsVetoTracks")),
        maxdxyTightMult = cms.double(1.0),
        corrTimeNeg = cms.double(-10),
        offTimePosTight = cms.double(25.0),
        maxdzLooseMult = cms.double(0.1),
        maxvertZ = cms.double(20),
        nChamberMatches = cms.int32(1),
        corrTimePos = cms.double(5),
        offTimeNegLoose = cms.double(-15.0),
        maxdxyLooseMult = cms.double(0.01),
        offTimePosTightMult = cms.double(25.0),
        offTimePosLoose = cms.double(15.0),
        largedxyMult = cms.double(3.0),
        largedxy = cms.double(2.0),
        nTrackThreshold = cms.int32(3),
        maxdzTightMult = cms.double(10.0),
        InputCosmicMuonCollection = cms.InputTag("muonsFromCosmics1Leg"),
        minvProb = cms.double(0.001),
        hIpTrdxy = cms.double(0.02),
        InputVertexCollection = cms.InputTag("offlinePrimaryVertices"),
        offTimePosLooseMult = cms.double(15.0),
        offTimeNegLooseMult = cms.double(-15.0),
        sharedHits = cms.int32(5),
        maxdxyLoose = cms.double(0.01),
        offTimeNegTightMult = cms.double(-20.0)
    ),
    muonCollection = cms.InputTag("muons1stStep"),
    trackCollections = cms.VInputTag(cms.InputTag("generalTracks"), cms.InputTag("cosmicsVetoTracks"))
)


process.cosmicsVetoSeeds = cms.EDProducer("TrajectorySeedFromMuonProducer",
    skipMatchedMuons = cms.bool(False),
    muonCollectionTag = cms.InputTag("muons1stStep"),
    trackCollectionTag = cms.InputTag("generalTracks")
)


process.cosmicsVetoTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("cosmicsVetoSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('none'),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilderP5')
)


process.cosmicsVetoTracks = cms.EDProducer("CosmicTrackSelector",
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    minNumber3DLayers = cms.uint32(0),
    src = cms.InputTag("cosmicsVetoTracksRaw"),
    copyExtras = cms.untracked.bool(True),
    min_pt = cms.double(1.0),
    copyTrajectories = cms.untracked.bool(True),
    qualityBit = cms.string(''),
    minNumberLayers = cms.uint32(0),
    chi2n_par = cms.double(10.0),
    max_eta = cms.double(2.0),
    min_nPixelHit = cms.uint32(0),
    min_nHit = cms.uint32(5),
    max_z0 = cms.double(300.0),
    beamspot = cms.InputTag("offlineBeamSpot")
)


process.cosmicsVetoTracksRaw = cms.EDProducer("TrackProducer",
    src = cms.InputTag("cosmicsVetoTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.cosmicseedfinder = cms.EDProducer("CosmicSeedGenerator",
    originRadius = cms.double(150.0),
    originHalfLength = cms.double(90.0),
    originZPosition = cms.double(0.0),
    GeometricStructure = cms.untracked.string('STANDARD'),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    SeedPt = cms.double(5.0),
    HitsForSeeds = cms.untracked.string('pairs'),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    NegativeYOnly = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    PositiveYOnly = cms.bool(False),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    MaxNumberOfPixelClusters = cms.uint32(300),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    ptMin = cms.double(0.9)
)


process.cosmicseedfinderP5 = cms.EDProducer("CosmicSeedGenerator",
    originRadius = cms.double(150.0),
    originHalfLength = cms.double(90.0),
    originZPosition = cms.double(0.0),
    GeometricStructure = cms.untracked.string('STANDARD'),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    SeedPt = cms.double(5.0),
    HitsForSeeds = cms.untracked.string('pairs'),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    NegativeYOnly = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    PositiveYOnly = cms.bool(False),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    MaxNumberOfPixelClusters = cms.uint32(300),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    ptMin = cms.double(0.9)
)


process.cosmicseedfinderP5Bottom = cms.EDProducer("CosmicSeedGenerator",
    originRadius = cms.double(150.0),
    originHalfLength = cms.double(90.0),
    originZPosition = cms.double(0.0),
    GeometricStructure = cms.untracked.string('STANDARD'),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    SeedPt = cms.double(5.0),
    HitsForSeeds = cms.untracked.string('pairs'),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit"),
    NegativeYOnly = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    PositiveYOnly = cms.bool(False),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    MaxNumberOfPixelClusters = cms.uint32(300),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    ClusterCollectionLabel = cms.InputTag("siStripClustersBottom"),
    ptMin = cms.double(0.9)
)


process.cosmicseedfinderP5Top = cms.EDProducer("CosmicSeedGenerator",
    originRadius = cms.double(150.0),
    originHalfLength = cms.double(90.0),
    originZPosition = cms.double(0.0),
    GeometricStructure = cms.untracked.string('STANDARD'),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    SeedPt = cms.double(5.0),
    HitsForSeeds = cms.untracked.string('pairs'),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    NegativeYOnly = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    PositiveYOnly = cms.bool(True),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    MaxNumberOfPixelClusters = cms.uint32(300),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    ClusterCollectionLabel = cms.InputTag("siStripClustersTop"),
    ptMin = cms.double(0.9)
)


process.cosmictrackSelector = cms.EDProducer("CosmicTrackSelector",
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    minNumber3DLayers = cms.uint32(0),
    src = cms.InputTag("ctfWithMaterialTracksCosmics"),
    copyExtras = cms.untracked.bool(True),
    min_pt = cms.double(1.0),
    copyTrajectories = cms.untracked.bool(True),
    qualityBit = cms.string(''),
    minNumberLayers = cms.uint32(0),
    chi2n_par = cms.double(10.0),
    max_eta = cms.double(2.0),
    min_nPixelHit = cms.uint32(0),
    min_nHit = cms.uint32(5),
    max_z0 = cms.double(300.0),
    beamspot = cms.InputTag("offlineBeamSpot")
)


process.cosmictrackfinderCosmics = cms.EDProducer("TrackProducer",
    src = cms.InputTag("cosmicCandidateFinderP5"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('cosmic'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.cosmictrackfinderP5 = cms.EDProducer("CosmicTrackSelector",
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    minNumber3DLayers = cms.uint32(0),
    src = cms.InputTag("cosmictrackfinderCosmics"),
    copyExtras = cms.untracked.bool(True),
    min_pt = cms.double(1.0),
    copyTrajectories = cms.untracked.bool(True),
    qualityBit = cms.string(''),
    minNumberLayers = cms.uint32(0),
    chi2n_par = cms.double(10.0),
    max_eta = cms.double(2.0),
    min_nPixelHit = cms.uint32(0),
    min_nHit = cms.uint32(5),
    max_z0 = cms.double(300.0),
    beamspot = cms.InputTag("offlineBeamSpot")
)


process.cosmictrackfinderP5Bottom = cms.EDProducer("TrackProducer",
    src = cms.InputTag("cosmicCandidateFinderP5Bottom"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerBottom"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('cosmic'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.cosmictrackfinderP5Top = cms.EDProducer("TrackProducer",
    src = cms.InputTag("cosmicCandidateFinderP5Top"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerTop"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('cosmic'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfCombinedSeeds = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesCombinedSeeds"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfNoOverlaps = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesNoOverlaps"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfPixelLess = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesPixelLess"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfWithMaterialTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfWithMaterialTracksCosmics = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesP5"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfWithMaterialTracksP5 = cms.EDProducer("CosmicTrackSelector",
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    minNumber3DLayers = cms.uint32(0),
    src = cms.InputTag("ctfWithMaterialTracksCosmics"),
    copyExtras = cms.untracked.bool(True),
    min_pt = cms.double(1.0),
    copyTrajectories = cms.untracked.bool(True),
    qualityBit = cms.string(''),
    minNumberLayers = cms.uint32(0),
    chi2n_par = cms.double(10.0),
    max_eta = cms.double(2.0),
    min_nPixelHit = cms.uint32(0),
    min_nHit = cms.uint32(5),
    max_z0 = cms.double(300.0),
    beamspot = cms.InputTag("offlineBeamSpot")
)


process.ctfWithMaterialTracksP5Bottom = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesP5Bottom"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerBottom"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfWithMaterialTracksP5LHCNavigation = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesP5LHCNavigation"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfWithMaterialTracksP5Top = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesP5Top"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerTop"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.dedxASmi = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    UsePixel = cms.bool(True),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    MaxNrStrips = cms.untracked.uint32(255),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxDiscrimASmi = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxDiscrimASmiCTF = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("ctfWithMaterialTracksP5"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("ctfWithMaterialTracksP5")
)


process.dedxDiscrimASmiCTFP5LHC = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation")
)


process.dedxDiscrimASmiCosmicTF = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("cosmictrackfinderP5"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("cosmictrackfinderP5")
)


process.dedxDiscrimASmiRS = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("rsWithMaterialTracksP5"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("rsWithMaterialTracksP5")
)


process.dedxDiscrimBTag = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(1),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxDiscrimProd = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(0),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxDiscrimSmi = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(2),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxHarm2 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter"),
    UsePixel = cms.bool(True),
    exponent = cms.double(-2.0)
)


process.dedxHarmonic2 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    trajectoryTrackAssociation = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    exponent = cms.double(-2.0)
)


process.dedxHarmonic2CTF = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("ctfWithMaterialTracksP5"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    exponent = cms.double(-2.0),
    trajectoryTrackAssociation = cms.InputTag("ctfWithMaterialTracksP5")
)


process.dedxHarmonic2CTFP5LHC = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    exponent = cms.double(-2.0),
    trajectoryTrackAssociation = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation")
)


process.dedxHarmonic2CosmicTF = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("cosmictrackfinderP5"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    exponent = cms.double(-2.0),
    trajectoryTrackAssociation = cms.InputTag("cosmictrackfinderP5")
)


process.dedxHarmonic2RS = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("rsWithMaterialTracksP5"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    exponent = cms.double(-2.0),
    trajectoryTrackAssociation = cms.InputTag("rsWithMaterialTracksP5")
)


process.dedxHitInfo = cms.EDProducer("HSCPDeDxInfoProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    UsePixel = cms.bool(True),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    MaxNrStrips = cms.untracked.uint32(255),
    Formula = cms.untracked.uint32(0),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxMedian = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('median'),
    ShapeTest = cms.bool(False),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxNPASmi = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    MaxNrStrips = cms.untracked.uint32(255),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxNPHarm2 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    exponent = cms.double(-2.0),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxNPProd = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    MaxNrStrips = cms.untracked.uint32(255),
    Formula = cms.untracked.uint32(0),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxNPTru40 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxNSHarm2 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(False),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(True),
    exponent = cms.double(-2.0),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxNSTHarm2 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(False),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(True),
    exponent = cms.double(-2.0),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxNSTru40 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(False),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(True),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxProd = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    UsePixel = cms.bool(True),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    MaxNrStrips = cms.untracked.uint32(255),
    Formula = cms.untracked.uint32(0),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxTru40 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MisCalib_Mean = cms.untracked.double(1.0),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(True),
    calibrationPath = cms.string('file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root'),
    MisCalib_Sigma = cms.untracked.double(0.0),
    tracks = cms.InputTag("TrackRefitter"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(True),
    trajectoryTrackAssociation = cms.InputTag("TrackRefitter")
)


process.dedxTruncated40 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxTruncated40CTF = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("ctfWithMaterialTracksP5"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("ctfWithMaterialTracksP5")
)


process.dedxTruncated40CTFP5LHC = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation")
)


process.dedxTruncated40CosmicTF = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("cosmictrackfinderP5"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("cosmictrackfinderP5")
)


process.dedxTruncated40RS = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("rsWithMaterialTracksP5"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("rsWithMaterialTracksP5")
)


process.dedxUnbinned = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('unbinnedFit'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.detachedTripletStep = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(False),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("detachedTripletStepSelector","detachedTripletStepVtx"), cms.InputTag("detachedTripletStepSelector","detachedTripletStepTrk")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1, 1),
    FoundHitBonus = cms.double(5.0),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(0, 1)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("detachedTripletStepTracks"), cms.InputTag("detachedTripletStepTracks")),
    LostHitPenalty = cms.double(20.0),
    newQuality = cms.string('confirmed')
)


process.detachedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    trajectories = cms.InputTag("pixelPairStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("pixelPairStepSelector","pixelPairStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.detachedTripletStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            ComponentName = cms.string('PixelTripletLargeTipGenerator'),
            extraHitRPhitolerance = cms.double(0.0),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.0)
        ),
        SeedingLayers = cms.string('detachedTripletStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False),
        FilterAtHelixStage = cms.bool(False)
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(1.5),
            ptMin = cms.double(0.3),
            originHalfLength = cms.double(15.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.detachedTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("detachedTripletStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(3),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.3, 3.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.2, 3.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('detachedTripletStepVtxLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(1.3, 3.0),
        d0_par1 = cms.vdouble(1.2, 3.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(0),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('loose'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.6, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.6, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepTrkLoose'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.6, 4.0),
            d0_par1 = cms.vdouble(1.6, 4.0),
            preFilterName = cms.string(''),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.9, 3.0),
            dz_par2 = cms.vdouble(1.0, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepVtxTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('detachedTripletStepVtxLoose'),
            d0_par2 = cms.vdouble(1.0, 3.0),
            d0_par1 = cms.vdouble(0.95, 3.0),
            res_par = cms.vdouble(0.003, 0.001),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.5),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepTrkTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('detachedTripletStepTrkLoose'),
            d0_par2 = cms.vdouble(1.1, 4.0),
            d0_par1 = cms.vdouble(1.1, 4.0),
            res_par = cms.vdouble(0.003, 0.001),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.9, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.8, 3.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepVtx'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.9, 3.0),
            d0_par1 = cms.vdouble(0.85, 3.0),
            preFilterName = cms.string('detachedTripletStepVtxTight'),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(4),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.4),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.0, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.0, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepTrk'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.0, 4.0),
            d0_par1 = cms.vdouble(1.0, 4.0),
            preFilterName = cms.string('detachedTripletStepTrkTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.detachedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("detachedTripletStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    TrajectoryBuilder = cms.string('detachedTripletStepTrajectoryBuilder'),
    numHitsForSeedCleaner = cms.int32(50)
)


process.detachedTripletStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("detachedTripletStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter3'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.dt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    Reco4DAlgoName = cms.string('DTMeantimerPatternReco4D'),
    Reco4DAlgoConfig = cms.PSet(
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            doVdriftCorr = cms.bool(True),
            debug = cms.untracked.bool(False),
            tTrigModeConfig = cms.PSet(
                vPropWire = cms.double(24.4),
                doTOFCorrection = cms.bool(True),
                tofCorrType = cms.int32(0),
                wirePropCorrType = cms.int32(0),
                tTrigLabel = cms.string(''),
                doWirePropCorrection = cms.bool(True),
                doT0Correction = cms.bool(True),
                debug = cms.untracked.bool(False)
            ),
            maxTime = cms.double(420.0)
        ),
        Reco2DAlgoConfig = cms.PSet(
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(False),
                doVdriftCorr = cms.bool(True),
                debug = cms.untracked.bool(False),
                tTrigModeConfig = cms.PSet(
                    vPropWire = cms.double(24.4),
                    doTOFCorrection = cms.bool(True),
                    tofCorrType = cms.int32(0),
                    wirePropCorrType = cms.int32(0),
                    tTrigLabel = cms.string(''),
                    doWirePropCorrection = cms.bool(True),
                    doT0Correction = cms.bool(True),
                    debug = cms.untracked.bool(False)
                ),
                maxTime = cms.double(420.0)
            ),
            segmCleanerMode = cms.int32(2),
            perform_delta_rejecting = cms.bool(True),
            MaxT0 = cms.double(100.0),
            performT0_vdriftSegCorrection = cms.bool(False),
            AlphaMaxPhi = cms.double(1.0),
            MaxChi2 = cms.double(1.0),
            hit_afterT0_resolution = cms.double(0.03),
            MaxAllowedHits = cms.uint32(50),
            nSharedHitsMax = cms.int32(2),
            AlphaMaxTheta = cms.double(0.9),
            debug = cms.untracked.bool(False),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            MinT0 = cms.double(-100.0)
        ),
        Reco2DAlgoName = cms.string('DTMeantimerPatternReco'),
        perform_delta_rejecting = cms.bool(True),
        hit_afterT0_resolution = cms.double(0.03),
        performT0_vdriftSegCorrection = cms.bool(False),
        debug = cms.untracked.bool(False),
        nUnSharedHitsMin = cms.int32(2),
        AllDTRecHits = cms.bool(True),
        performT0SegCorrection = cms.bool(False)
    ),
    debug = cms.untracked.bool(False),
    recHits1DLabel = cms.InputTag("dt1DRecHits"),
    recHits2DLabel = cms.InputTag("dt2DSegments")
)


process.dt4DSegmentsMT = cms.EDProducer("DTRecSegment4DProducer",
    debug = cms.untracked.bool(False),
    Reco4DAlgoName = cms.string('DTMeantimerPatternReco4D'),
    recHits2DLabel = cms.InputTag("dt2DSegments"),
    recHits1DLabel = cms.InputTag("dt1DRecHits"),
    Reco4DAlgoConfig = cms.PSet(
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(True),
            doVdriftCorr = cms.bool(True),
            debug = cms.untracked.bool(False),
            tTrigModeConfig = cms.PSet(
                vPropWire = cms.double(24.4),
                doTOFCorrection = cms.bool(True),
                tofCorrType = cms.int32(0),
                wirePropCorrType = cms.int32(0),
                tTrigLabel = cms.string(''),
                doWirePropCorrection = cms.bool(True),
                doT0Correction = cms.bool(True),
                debug = cms.untracked.bool(False)
            ),
            maxTime = cms.double(420.0)
        ),
        Reco2DAlgoConfig = cms.PSet(
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(True),
                doVdriftCorr = cms.bool(True),
                debug = cms.untracked.bool(False),
                tTrigModeConfig = cms.PSet(
                    vPropWire = cms.double(24.4),
                    doTOFCorrection = cms.bool(True),
                    tofCorrType = cms.int32(0),
                    wirePropCorrType = cms.int32(0),
                    tTrigLabel = cms.string(''),
                    doWirePropCorrection = cms.bool(True),
                    doT0Correction = cms.bool(True),
                    debug = cms.untracked.bool(False)
                ),
                maxTime = cms.double(420.0)
            ),
            segmCleanerMode = cms.int32(2),
            perform_delta_rejecting = cms.bool(True),
            MaxT0 = cms.double(100.0),
            performT0_vdriftSegCorrection = cms.bool(False),
            AlphaMaxPhi = cms.double(1.0),
            MaxChi2 = cms.double(1.0),
            hit_afterT0_resolution = cms.double(0.03),
            MaxAllowedHits = cms.uint32(50),
            nSharedHitsMax = cms.int32(2),
            AlphaMaxTheta = cms.double(0.9),
            debug = cms.untracked.bool(False),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            MinT0 = cms.double(-100.0)
        ),
        Reco2DAlgoName = cms.string('DTMeantimerPatternReco'),
        perform_delta_rejecting = cms.bool(True),
        hit_afterT0_resolution = cms.double(0.03),
        performT0_vdriftSegCorrection = cms.bool(False),
        debug = cms.untracked.bool(False),
        nUnSharedHitsMin = cms.int32(2),
        AllDTRecHits = cms.bool(True),
        performT0SegCorrection = cms.bool(False)
    )
)


process.genParticles = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)


process.generalTracks = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(False),
    MinPT = cms.double(0.05),
    makeReKeyedSeeds = cms.untracked.bool(False),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("initialStepSelector","initialStep"), cms.InputTag("lowPtTripletStepSelector","lowPtTripletStep"), cms.InputTag("pixelPairStepSelector","pixelPairStep"), cms.InputTag("detachedTripletStep"), cms.InputTag("mixedTripletStep"), 
        cms.InputTag("pixelLessStepSelector","pixelLessStep"), cms.InputTag("tobTecStepSelector","tobTecStep")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1, 1, 1, 1, 1, 
        1, 1),
    FoundHitBonus = cms.double(5.0),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(0, 1, 2, 3, 4, 
            5, 6)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("initialStepTracks"), cms.InputTag("lowPtTripletStepTracks"), cms.InputTag("pixelPairStepTracks"), cms.InputTag("detachedTripletStepTracks"), cms.InputTag("mixedTripletStepTracks"), 
        cms.InputTag("pixelLessStepTracks"), cms.InputTag("tobTecStepTracks")),
    LostHitPenalty = cms.double(20.0),
    newQuality = cms.string('confirmed')
)


process.glbTrackQual = cms.EDProducer("GlobalTrackQualityProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double(0.0),
        DeltaDCut_3 = cms.double(15.0),
        MinP = cms.double(2.5),
        MinPt = cms.double(1.0),
        Chi2Cut_1 = cms.double(50.0),
        Pt_threshold2 = cms.double(999999999.0),
        LocChi2Cut = cms.double(20.0),
        Eta_threshold = cms.double(1.2),
        Quality_3 = cms.double(7.0),
        Quality_2 = cms.double(15.0),
        Chi2Cut_2 = cms.double(50.0),
        Chi2Cut_3 = cms.double(200.0),
        DeltaDCut_1 = cms.double(2.5),
        DeltaRCut_2 = cms.double(0.2),
        DeltaRCut_3 = cms.double(1.0),
        DeltaDCut_2 = cms.double(10.0),
        DeltaRCut_1 = cms.double(0.1),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        Quality_1 = cms.double(20.0)
    ),
    BaseLabel = cms.string('GLB'),
    MaxChi2 = cms.double(100000.0),
    nSigma = cms.double(3.0),
    InputCollection = cms.InputTag("globalMuons"),
    RefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32(-1),
        MuonHitsOption = cms.int32(1),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        RefitDirection = cms.string('insideOut'),
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        Propagator = cms.string('SmartPropagatorAnyRK'),
        TrackerSkipSystem = cms.int32(-1),
        DoPredictionsOnly = cms.bool(False),
        Chi2ProbabilityCut = cms.double(30.0),
        PropDirForCosmics = cms.bool(False),
        HitThreshold = cms.int32(1),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        Chi2CutCSC = cms.double(1.0),
        Chi2CutRPC = cms.double(1.0),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        DYTthrs = cms.vint32(10, 5),
        RefitRPCHits = cms.bool(True),
        Chi2CutDT = cms.double(30.0),
        PtCut = cms.double(1.0),
        SkipStation = cms.int32(-1)
    ),
    InputLinksCollection = cms.InputTag("globalMuons")
)


process.globalCombinedSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("globalSeedsFromTripletsWithVertices"), cms.InputTag("globalSeedsFromPairsWithVertices"))
)


process.globalCosmicMuons = cms.EDProducer("GlobalCosmicMuonProducer",
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        PutTrajectoryIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False),
        AllowNoVertex = cms.untracked.bool(True),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrajectoryBuilderParameters = cms.PSet(
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(20.0),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(2.5),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            Quality_1 = cms.double(20.0)
        ),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        TkTrackCollectionLabel = cms.InputTag("regionalCosmicTracks"),
        SmootherParameters = cms.PSet(
            PropagatorAlong = cms.string('SteppingHelixPropagatorAny'),
            PropagatorOpposite = cms.string('SteppingHelixPropagatorAny'),
            RescalingFactor = cms.double(5.0)
        ),
        Propagator = cms.string('SteppingHelixPropagatorAny')
    ),
    MuonCollectionLabel = cms.InputTag("cosmicMuons")
)


process.globalCosmicMuons1Leg = cms.EDProducer("GlobalCosmicMuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrajectoryBuilderParameters = cms.PSet(
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(20.0),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(2.5),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            Quality_1 = cms.double(20.0)
        ),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        TkTrackCollectionLabel = cms.InputTag("regionalCosmicTracks"),
        SmootherParameters = cms.PSet(
            PropagatorAlong = cms.string('SteppingHelixPropagatorAny'),
            PropagatorOpposite = cms.string('SteppingHelixPropagatorAny'),
            RescalingFactor = cms.double(5.0)
        ),
        Propagator = cms.string('SteppingHelixPropagatorAny')
    ),
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        PutTrajectoryIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False),
        AllowNoVertex = cms.untracked.bool(True),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False)
    ),
    MuonCollectionLabel = cms.InputTag("cosmicMuons1Leg")
)


process.globalMixedSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(21.2)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('MixedLayerPairs')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalMuons = cms.EDProducer("GlobalMuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False)
    ),
    GLBTrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        GlbRefitterParameters = cms.PSet(
            TrackerSkipSection = cms.int32(-1),
            DoPredictionsOnly = cms.bool(False),
            PropDirForCosmics = cms.bool(False),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('GlbMuKFFitter'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            TrackerRecHitBuilder = cms.string('WithTrackAngle'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DYTthrs = cms.vint32(30, 15),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            PtCut = cms.double(1.0),
            Chi2ProbabilityCut = cms.double(30.0),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        ScaleTECxFactor = cms.double(-1.0),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            OnDemand = cms.double(-1.0),
            Rescale_Dz = cms.double(3.0),
            Eta_min = cms.double(0.1),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            MeasurementTrackerName = cms.string(''),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            vertexCollection = cms.InputTag("pixelVertices"),
            Phi_fixed = cms.double(0.2),
            DeltaR = cms.double(0.2),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            Rescale_eta = cms.double(3.0),
            Phi_min = cms.double(0.1),
            UseVertex = cms.bool(False),
            beamSpot = cms.InputTag("offlineBeamSpot")
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('KFFitterForRefitInsideOut'),
            TrackerRecHitBuilder = cms.string('WithTrackAngle'),
            Smoother = cms.string('KFSmootherForRefitInsideOut'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            RefitDirection = cms.string('alongMomentum'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('SmartPropagatorAnyRK')
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(20.0),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(2.5),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('SmartPropagatorRK'),
            Quality_1 = cms.double(20.0)
        ),
        PtCut = cms.double(1.0),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny')
    ),
    TrackerCollectionLabel = cms.InputTag("generalTracks"),
    MuonCollectionLabel = cms.InputTag("standAloneMuons","UpdatedAtVtx")
)


process.globalPixelLessSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(40)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(5000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('pixelLessLayerPairs4PixelLessTracking')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalPixelSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(21.2)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('PixelLayerPairs')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalSETMuons = cms.EDProducer("GlobalMuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    GLBTrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        GlbRefitterParameters = cms.PSet(
            TrackerSkipSection = cms.int32(-1),
            DoPredictionsOnly = cms.bool(False),
            PropDirForCosmics = cms.bool(False),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('GlbMuKFFitter'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            TrackerRecHitBuilder = cms.string('WithTrackAngle'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            DYTthrs = cms.vint32(30, 15),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            PtCut = cms.double(1.0),
            Chi2ProbabilityCut = cms.double(30.0),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('SmartPropagatorAnyRK'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        ScaleTECxFactor = cms.double(-1.0),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            OnDemand = cms.double(-1.0),
            Rescale_Dz = cms.double(3.0),
            Eta_min = cms.double(0.1),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            MeasurementTrackerName = cms.string(''),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            vertexCollection = cms.InputTag("pixelVertices"),
            Phi_fixed = cms.double(0.2),
            DeltaR = cms.double(0.2),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            Rescale_eta = cms.double(3.0),
            Phi_min = cms.double(0.1),
            UseVertex = cms.bool(False),
            beamSpot = cms.InputTag("offlineBeamSpot")
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('KFFitterForRefitInsideOut'),
            TrackerRecHitBuilder = cms.string('WithTrackAngle'),
            Smoother = cms.string('KFSmootherForRefitInsideOut'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            RefitDirection = cms.string('alongMomentum'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('SmartPropagatorAnyRK')
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(20.0),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(2.5),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('SmartPropagatorRK'),
            Quality_1 = cms.double(20.0)
        ),
        PtCut = cms.double(1.0),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny')
    ),
    TrackerCollectionLabel = cms.InputTag("generalTracks"),
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False)
    ),
    MuonCollectionLabel = cms.InputTag("standAloneSETMuons","UpdatedAtVtx")
)


process.globalSeedsFromPairsWithVertices = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            useFixedError = cms.bool(True),
            originRadius = cms.double(0.2),
            sigmaZVertex = cms.double(3.0),
            fixedError = cms.double(0.2),
            VertexCollection = cms.InputTag("pixelVertices"),
            ptMin = cms.double(0.9),
            useFoundVertices = cms.bool(True),
            nSigmaZ = cms.double(4.0)
        ),
        ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('MixedLayerPairs')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalSeedsFromTriplets = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(21.2)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('PixelLayerTriplets')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.initialStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    trajectories = cms.InputTag("initialStepSeeds"),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.initialStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('PixelLayerTriplets')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(0.02),
            nSigmaZ = cms.double(4.0),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            ptMin = cms.double(0.6)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.initialStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("initialStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(0),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(0.45, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(0.65, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('initialStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.01),
        d0_par2 = cms.vdouble(0.55, 4.0),
        d0_par1 = cms.vdouble(0.55, 4.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('initialStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('initialStepLoose'),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            res_par = cms.vdouble(0.003, 0.01),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.35, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('initialStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            preFilterName = cms.string('initialStepTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.initialStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("initialStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    TrajectoryBuilder = cms.string('initialStepTrajectoryBuilder'),
    numHitsForSeedCleaner = cms.int32(50)
)


process.initialStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("initialStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter0'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.isoDeposits = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag(""),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag(""),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.lowPtTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    trajectories = cms.InputTag("initialStepTracks"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("initialStepSelector","initialStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.lowPtTripletStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('lowPtTripletStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(0.02),
            nSigmaZ = cms.double(4.0),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            ptMin = cms.double(0.2)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.lowPtTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("lowPtTripletStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(0),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(0.45, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(0.65, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('lowPtTripletStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.01),
        d0_par2 = cms.vdouble(0.55, 4.0),
        d0_par1 = cms.vdouble(0.55, 4.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('lowPtTripletStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('lowPtTripletStepLoose'),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            res_par = cms.vdouble(0.003, 0.01),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.35, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('lowPtTripletStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            preFilterName = cms.string('lowPtTripletStepTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.lowPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("lowPtTripletStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    TrajectoryBuilder = cms.string('lowPtTripletStepTrajectoryBuilder'),
    numHitsForSeedCleaner = cms.int32(50)
)


process.lowPtTripletStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("lowPtTripletStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter1'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.mergedStandAloneMuonSeeds = cms.EDProducer("MuonSeedMerger",
    SeedCollections = cms.VInputTag(cms.InputTag("ancientMuonSeed"), cms.InputTag("MuonSeed"))
)


process.mixedTripletStep = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(False),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("mixedTripletStepSelector","mixedTripletStepVtx"), cms.InputTag("mixedTripletStepSelector","mixedTripletStepTrk")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1, 1),
    FoundHitBonus = cms.double(5.0),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(0, 1)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("mixedTripletStepTracks"), cms.InputTag("mixedTripletStepTracks")),
    LostHitPenalty = cms.double(20.0),
    newQuality = cms.string('confirmed')
)


process.mixedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    trajectories = cms.InputTag("detachedTripletStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("detachedTripletStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.mixedTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    trajectories = cms.InputTag("mixedTripletStepSeeds"),
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepSeedClusterMask"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.mixedTripletStepSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"), cms.InputTag("mixedTripletStepSeedsB"))
)


process.mixedTripletStepSeedsA = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            ComponentName = cms.string('PixelTripletLargeTipGenerator'),
            extraHitRPhitolerance = cms.double(0.0),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.0)
        ),
        SeedingLayers = cms.string('mixedTripletStepSeedLayersA')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True),
        FilterAtHelixStage = cms.bool(False)
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(1.5),
            ptMin = cms.double(0.4),
            originHalfLength = cms.double(10.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.mixedTripletStepSeedsB = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            ComponentName = cms.string('PixelTripletLargeTipGenerator'),
            extraHitRPhitolerance = cms.double(0.0),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.0)
        ),
        SeedingLayers = cms.string('mixedTripletStepSeedLayersB')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True),
        FilterAtHelixStage = cms.bool(False)
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(1.5),
            ptMin = cms.double(0.6),
            originHalfLength = cms.double(10.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.mixedTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("mixedTripletStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(2),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(3),
        chi2n_par = cms.double(1.2),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.3, 3.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.2, 3.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('mixedTripletStepVtxLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(1.3, 3.0),
        d0_par1 = cms.vdouble(1.2, 3.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('loose'),
            minNumberLayers = cms.uint32(4),
            chi2n_par = cms.double(0.6),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.2, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.2, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepTrkLoose'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.2, 4.0),
            d0_par1 = cms.vdouble(1.2, 4.0),
            preFilterName = cms.string(''),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.6),
            dz_par1 = cms.vdouble(1.1, 3.0),
            dz_par2 = cms.vdouble(1.2, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepVtxTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('mixedTripletStepVtxLoose'),
            d0_par2 = cms.vdouble(1.2, 3.0),
            d0_par1 = cms.vdouble(1.1, 3.0),
            res_par = cms.vdouble(0.003, 0.001),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(4),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.4),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepTrkTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('mixedTripletStepTrkLoose'),
            d0_par2 = cms.vdouble(1.1, 4.0),
            d0_par1 = cms.vdouble(1.1, 4.0),
            res_par = cms.vdouble(0.003, 0.001),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.4),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.2, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.1, 3.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepVtx'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.2, 3.0),
            d0_par1 = cms.vdouble(1.1, 3.0),
            preFilterName = cms.string('mixedTripletStepVtxTight'),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(4),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.3),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.9, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.9, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepTrk'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.9, 4.0),
            d0_par1 = cms.vdouble(0.9, 4.0),
            preFilterName = cms.string('mixedTripletStepTrkTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.mixedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("mixedTripletStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    numHitsForSeedCleaner = cms.int32(50),
    TrajectoryBuilder = cms.string('mixedTripletStepTrajectoryBuilder')
)


process.mixedTripletStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("mixedTripletStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter4'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.muIsoDepositCalByAssociatorHits = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("muons1stStep"),
        MultipleDepositsFlag = cms.bool(True),
        MuonTrackRefType = cms.string('bestTrkSta'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.025),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.1),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(True),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(False),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(True)
        ),
        Threshold_HO = cms.double(0.1),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    )
)


process.muIsoDepositCalByAssociatorTowers = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring('ecal', 
        'hcal', 
        'ho'),
    inputTags = cms.VInputTag(cms.InputTag("muons1stStep","ecal"), cms.InputTag("muons1stStep","hcal"), cms.InputTag("muons1stStep","ho"))
)


process.muIsoDepositJets = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(''),
    inputTags = cms.VInputTag(cms.InputTag("muons1stStep","jets"))
)


process.muIsoDepositTk = cms.EDProducer("MuIsoDepositCopyProducer",
    depositNames = cms.vstring(''),
    inputTags = cms.VInputTag(cms.InputTag("muons1stStep","tracker"))
)


process.muPFIsoDepositCharged = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("muons1stStep"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositChargedAll = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("muons1stStep"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticles"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositGamma = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("muons1stStep"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositNeutral = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("muons1stStep"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositPU = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("muons1stStep"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticles"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositCharged"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositCharged"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositGamma"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositGamma"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueGammaHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositGamma"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueGammaHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositGamma"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositNeutral"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositNeutral"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueNeutralHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositNeutral"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueNeutralHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositNeutral"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositPU"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositPU"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muParamGlobalIsoDepositCalByAssociatorHits = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(True),
        MuonTrackRefType = cms.string('bestTrkSta'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.025),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.1),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(True),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(False),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(True)
        ),
        Threshold_HO = cms.double(0.1),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    )
)


process.muParamGlobalIsoDepositCalByAssociatorTowers = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(True),
        MuonTrackRefType = cms.string('bestTrkSta'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.2),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.5),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    )
)


process.muParamGlobalIsoDepositCalEcal = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        DR_Veto_H = cms.double(0.1),
        Vertex_Constraint_Z = cms.bool(False),
        Threshold_H = cms.double(0.5),
        ComponentName = cms.string('CaloExtractor'),
        Threshold_E = cms.double(0.2),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        Weight_E = cms.double(1.0),
        Vertex_Constraint_XY = cms.bool(False),
        DepositLabel = cms.untracked.string('EcalPlusHcal'),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        Weight_H = cms.double(0.0)
    )
)


process.muParamGlobalIsoDepositCalHcal = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        DR_Veto_H = cms.double(0.1),
        Vertex_Constraint_Z = cms.bool(False),
        Threshold_H = cms.double(0.5),
        ComponentName = cms.string('CaloExtractor'),
        Threshold_E = cms.double(0.2),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        Weight_E = cms.double(0.0),
        Vertex_Constraint_XY = cms.bool(False),
        DepositLabel = cms.untracked.string('EcalPlusHcal'),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        Weight_H = cms.double(1.0)
    )
)


process.muParamGlobalIsoDepositCtfTk = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('bestTrkSta'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("ctfGSWithMaterialTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    )
)


process.muParamGlobalIsoDepositGsTk = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("ctfGSWithMaterialTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    )
)


process.muParamGlobalIsoDepositJets = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('bestTrkSta'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(0.5),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("ak5CaloJets"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    )
)


process.muParamGlobalIsoDepositTk = cms.EDProducer("MuIsoDepositProducer",
    IOPSet = cms.PSet(
        ExtractForCandidate = cms.bool(False),
        inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
        MultipleDepositsFlag = cms.bool(False),
        MuonTrackRefType = cms.string('track'),
        InputType = cms.string('MuonCollection')
    ),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("generalTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    )
)


process.muidAllArbitrated = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('AllArbitrated')
)


process.muidGMStaChiCompatibility = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GMStaChiCompatibility')
)


process.muidGMTkChiCompatibility = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GMTkChiCompatibility')
)


process.muidGMTkKinkTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GMTkKinkTight')
)


process.muidGlobalMuonPromptTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('GlobalMuonPromptTight')
)


process.muidTM2DCompatibilityLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TM2DCompatibilityLoose')
)


process.muidTM2DCompatibilityTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TM2DCompatibilityTight')
)


process.muidTMLastStationAngLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationAngLoose')
)


process.muidTMLastStationAngTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationAngTight')
)


process.muidTMLastStationLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationLoose')
)


process.muidTMLastStationOptimizedLowPtLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationOptimizedLowPtLoose')
)


process.muidTMLastStationOptimizedLowPtTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationOptimizedLowPtTight')
)


process.muidTMLastStationTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMLastStationTight')
)


process.muidTMOneStationAngLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationAngLoose')
)


process.muidTMOneStationAngTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationAngTight')
)


process.muidTMOneStationLoose = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationLoose')
)


process.muidTMOneStationTight = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TMOneStationTight')
)


process.muidTrackerMuonArbitrated = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('TrackerMuonArbitrated')
)


process.muonEcalDetIds = cms.EDProducer("InterestingEcalDetIdProducer",
    inputCollection = cms.InputTag("muons1stStep")
)


process.muonSelectionTypeValueMapProducer = cms.EDProducer("MuonSelectionTypeValueMapProducer",
    inputMuonCollection = cms.InputTag("muons1stStep"),
    selectionType = cms.string('All')
)


process.muonShowerInformation = cms.EDProducer("MuonShowerInformationProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    trackCollection = cms.InputTag("generalTracks"),
    ShowerInformationFillerParameters = cms.PSet(
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                'SteppingHelixPropagatorAlong', 
                'SteppingHelixPropagatorOpposite', 
                'SteppingHelixPropagatorL2Any', 
                'SteppingHelixPropagatorL2Along', 
                'SteppingHelixPropagatorL2Opposite', 
                'SteppingHelixPropagatorAnyNoError', 
                'SteppingHelixPropagatorAlongNoError', 
                'SteppingHelixPropagatorOppositeNoError', 
                'SteppingHelixPropagatorL2AnyNoError', 
                'SteppingHelixPropagatorL2AlongNoError', 
                'SteppingHelixPropagatorL2OppositeNoError', 
                'PropagatorWithMaterial', 
                'PropagatorWithMaterialOpposite', 
                'SmartPropagator', 
                'SmartPropagatorOpposite', 
                'SmartPropagatorAnyOpposite', 
                'SmartPropagatorAny', 
                'SmartPropagatorRK', 
                'SmartPropagatorAnyRK', 
                'StraightLinePropagator'),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        DT4DRecSegmentLabel = cms.InputTag("dt4DSegments"),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        CSCSegmentLabel = cms.InputTag("cscSegments"),
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
    ),
    muonCollection = cms.InputTag("muons1stStep")
)


process.muons = cms.EDProducer("MuonProducer",
    EcalIsoDeposits = cms.InputTag("muIsoDepositCalByAssociatorTowers","ecal"),
    ShowerInfoMap = cms.InputTag("muonShowerInformation"),
    FillTimingInfo = cms.bool(True),
    FillSelectorMaps = cms.bool(True),
    TrackIsoDeposits = cms.InputTag("muIsoDepositTk"),
    InputMuons = cms.InputTag("muons1stStep"),
    FillDetectorBasedIsolation = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowTmp"),
    JetIsoDeposits = cms.InputTag("muIsoDepositJets"),
    PFIsolation = cms.PSet(
        isolationR04 = cms.PSet(
            photonHighThreshold = cms.InputTag("muPFIsoValueGammaHighThreshold04"),
            pu = cms.InputTag("muPFIsoValuePU04"),
            neutralHadronHighThreshold = cms.InputTag("muPFIsoValueNeutralHighThreshold04"),
            chargedParticle = cms.InputTag("muPFIsoValueChargedAll04"),
            photon = cms.InputTag("muPFIsoValueGamma04"),
            chargedHadron = cms.InputTag("muPFIsoValueCharged04"),
            neutralHadron = cms.InputTag("muPFIsoValueNeutral04")
        ),
        isolationR03 = cms.PSet(
            photonHighThreshold = cms.InputTag("muPFIsoValueGammaHighThreshold03"),
            pu = cms.InputTag("muPFIsoValuePU03"),
            neutralHadronHighThreshold = cms.InputTag("muPFIsoValueNeutralHighThreshold03"),
            chargedParticle = cms.InputTag("muPFIsoValueChargedAll03"),
            photon = cms.InputTag("muPFIsoValueGamma03"),
            chargedHadron = cms.InputTag("muPFIsoValueCharged03"),
            neutralHadron = cms.InputTag("muPFIsoValueNeutral03")
        )
    ),
    FillCosmicsIdMap = cms.bool(True),
    HoIsoDeposits = cms.InputTag("muIsoDepositCalByAssociatorTowers","ho"),
    HcalIsoDeposits = cms.InputTag("muIsoDepositCalByAssociatorTowers","hcal"),
    ActivateDebug = cms.untracked.bool(False),
    FillPFIsolation = cms.bool(True),
    CosmicIdMap = cms.InputTag("cosmicsVeto"),
    FillPFMomentumAndAssociation = cms.bool(True),
    FillShoweringInfo = cms.bool(True),
    SelectorMaps = cms.VInputTag(cms.InputTag("muidTMLastStationOptimizedLowPtLoose"), cms.InputTag("muidTMLastStationOptimizedLowPtTight"), cms.InputTag("muidTM2DCompatibilityLoose"), cms.InputTag("muidTM2DCompatibilityTight"), cms.InputTag("muidTrackerMuonArbitrated"), 
        cms.InputTag("muidTMLastStationAngLoose"), cms.InputTag("muidGlobalMuonPromptTight"), cms.InputTag("muidGMStaChiCompatibility"), cms.InputTag("muidTMLastStationAngTight"), cms.InputTag("muidGMTkChiCompatibility"), 
        cms.InputTag("muidTMOneStationAngTight"), cms.InputTag("muidTMOneStationAngLoose"), cms.InputTag("muidTMLastStationLoose"), cms.InputTag("muidTMLastStationTight"), cms.InputTag("muidTMOneStationTight"), 
        cms.InputTag("muidTMOneStationLoose"), cms.InputTag("muidAllArbitrated"), cms.InputTag("muidGMTkKinkTight"))
)


process.muons1stStep = cms.EDProducer("MuonIdProducer",
    MuonCaloCompatibility = cms.PSet(
        allSiPMHO = cms.bool(False),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("generalTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    ecalDepositName = cms.string('ecal'),
    JetExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(0.5),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("ak5CaloJets"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    ),
    hcalDepositName = cms.string('hcal'),
    trackDepositName = cms.string('tracker'),
    CaloExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.2),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.5),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    ),
    jetDepositName = cms.string('jets'),
    hoDepositName = cms.string('ho'),
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(6.0),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        usePosition = cms.bool(True),
        diagonalOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite')
    ),
    maxAbsEta = cms.double(3.0),
    fillGlobalTrackRefits = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        ClusterDPhi = cms.double(0.6),
        OverlapDTheta = cms.double(0.02),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        ClusterDTheta = cms.double(0.02)
    ),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    addExtraSoftMuons = cms.bool(False),
    debugWithTruthMatching = cms.bool(False),
    runArbitrationCleaner = cms.bool(True),
    fillEnergy = cms.bool(True),
    inputCollectionTypes = cms.vstring('inner tracks', 
        'links', 
        'outer tracks', 
        'tev firstHit', 
        'tev picky', 
        'tev dyt'),
    minCaloCompatibility = cms.double(0.6),
    fillCaloCompatibility = cms.bool(True),
    minP = cms.double(2.5),
    fillIsolation = cms.bool(True),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    writeIsoDeposits = cms.bool(True),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minPt = cms.double(0.5),
    minPCaloMuon = cms.double(1.0),
    fillMatching = cms.bool(True),
    fillTrackerKink = cms.bool(True),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    inputCollectionLabels = cms.VInputTag(cms.InputTag("generalTracks"), cms.InputTag("globalMuons"), cms.InputTag("standAloneMuons","UpdatedAtVtx"), cms.InputTag("tevMuons","firstHit"), cms.InputTag("tevMuons","picky"), 
        cms.InputTag("tevMuons","dyt")),
    fillGlobalTrackQuality = cms.bool(True),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    minNumberOfMatches = cms.int32(1)
)


process.muonsFromCosmics = cms.EDProducer("MuonIdProducer",
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("regionalCosmicTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    maxAbsEta = cms.double(3.0),
    fillGlobalTrackRefits = cms.bool(False),
    arbitrationCleanerOptions = cms.PSet(
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        ClusterDPhi = cms.double(0.6),
        OverlapDTheta = cms.double(0.02),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        ClusterDTheta = cms.double(0.02)
    ),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    addExtraSoftMuons = cms.bool(False),
    debugWithTruthMatching = cms.bool(False),
    CaloExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.2),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.5),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    ),
    runArbitrationCleaner = cms.bool(True),
    fillEnergy = cms.bool(True),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        usePosition = cms.bool(True),
        diagonalOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite')
    ),
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DCosmicSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(6.0),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DCosmicSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DCosmicSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    inputCollectionTypes = cms.vstring('links', 
        'outer tracks', 
        'inner tracks'),
    minCaloCompatibility = cms.double(0.6),
    ecalDepositName = cms.string('ecal'),
    minP = cms.double(2.5),
    fillIsolation = cms.bool(False),
    jetDepositName = cms.string('jets'),
    hoDepositName = cms.string('ho'),
    writeIsoDeposits = cms.bool(True),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minPt = cms.double(0.5),
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DCosmicSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    JetExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(0.5),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("ak5CaloJets"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    ),
    fillGlobalTrackQuality = cms.bool(False),
    minPCaloMuon = cms.double(1.0),
    maxAbsDy = cms.double(9999.0),
    fillCaloCompatibility = cms.bool(True),
    fillMatching = cms.bool(True),
    MuonCaloCompatibility = cms.PSet(
        allSiPMHO = cms.bool(False),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    fillTrackerKink = cms.bool(True),
    hcalDepositName = cms.string('hcal'),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    inputCollectionLabels = cms.VInputTag("globalCosmicMuons", "cosmicMuons", "regionalCosmicTracks"),
    trackDepositName = cms.string('tracker'),
    maxAbsDx = cms.double(3.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    minNumberOfMatches = cms.int32(1)
)


process.muonsFromCosmics1Leg = cms.EDProducer("MuonIdProducer",
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("regionalCosmicTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    maxAbsEta = cms.double(3.0),
    fillGlobalTrackRefits = cms.bool(False),
    arbitrationCleanerOptions = cms.PSet(
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        ClusterDPhi = cms.double(0.6),
        OverlapDTheta = cms.double(0.02),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        ClusterDTheta = cms.double(0.02)
    ),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    addExtraSoftMuons = cms.bool(False),
    debugWithTruthMatching = cms.bool(False),
    CaloExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.2),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.5),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    ),
    runArbitrationCleaner = cms.bool(True),
    fillEnergy = cms.bool(True),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        usePosition = cms.bool(True),
        diagonalOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite')
    ),
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DCosmicSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(6.0),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DCosmicSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DCosmicSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    inputCollectionTypes = cms.vstring('links', 
        'outer tracks', 
        'inner tracks'),
    minCaloCompatibility = cms.double(0.6),
    ecalDepositName = cms.string('ecal'),
    minP = cms.double(2.5),
    fillIsolation = cms.bool(False),
    jetDepositName = cms.string('jets'),
    hoDepositName = cms.string('ho'),
    writeIsoDeposits = cms.bool(True),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minPt = cms.double(0.5),
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DCosmicSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    JetExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(0.5),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("ak5CaloJets"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    ),
    fillGlobalTrackQuality = cms.bool(False),
    minPCaloMuon = cms.double(1.0),
    maxAbsDy = cms.double(9999.0),
    fillCaloCompatibility = cms.bool(True),
    fillMatching = cms.bool(True),
    MuonCaloCompatibility = cms.PSet(
        allSiPMHO = cms.bool(False),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    fillTrackerKink = cms.bool(True),
    hcalDepositName = cms.string('hcal'),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    inputCollectionLabels = cms.VInputTag("globalCosmicMuons1Leg", "cosmicMuons1Leg", "regionalCosmicTracks"),
    trackDepositName = cms.string('tracker'),
    maxAbsDx = cms.double(3.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    minNumberOfMatches = cms.int32(1)
)


process.muonsWithSET = cms.EDProducer("MuonIdProducer",
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("generalTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    maxAbsEta = cms.double(3.0),
    fillGlobalTrackRefits = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        ClusterDPhi = cms.double(0.6),
        OverlapDTheta = cms.double(0.02),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        ClusterDTheta = cms.double(0.02)
    ),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    addExtraSoftMuons = cms.bool(False),
    debugWithTruthMatching = cms.bool(False),
    CaloExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.2),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.5),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    ),
    runArbitrationCleaner = cms.bool(True),
    fillEnergy = cms.bool(True),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        usePosition = cms.bool(True),
        diagonalOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite')
    ),
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(6.0),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    inputCollectionTypes = cms.vstring('inner tracks', 
        'links', 
        'outer tracks'),
    minCaloCompatibility = cms.double(0.6),
    ecalDepositName = cms.string('ecal'),
    minP = cms.double(2.5),
    fillIsolation = cms.bool(True),
    jetDepositName = cms.string('jets'),
    hoDepositName = cms.string('ho'),
    writeIsoDeposits = cms.bool(True),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minPt = cms.double(0.5),
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    JetExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(0.5),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("ak5CaloJets"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    ),
    fillGlobalTrackQuality = cms.bool(True),
    minPCaloMuon = cms.double(1.0),
    maxAbsDy = cms.double(9999.0),
    fillCaloCompatibility = cms.bool(True),
    fillMatching = cms.bool(True),
    MuonCaloCompatibility = cms.PSet(
        allSiPMHO = cms.bool(False),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    fillTrackerKink = cms.bool(True),
    hcalDepositName = cms.string('hcal'),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    inputCollectionLabels = cms.VInputTag("generalTracks", "globalSETMuons", cms.InputTag("standAloneSETMuons","UpdatedAtVtx")),
    trackDepositName = cms.string('tracker'),
    maxAbsDx = cms.double(3.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    minNumberOfMatches = cms.int32(1)
)


process.muontiming = cms.EDProducer("MuonTimingProducer",
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegmentsMT"),
                DTradius = cms.double(1.0),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(3),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(False)
    ),
    MuonCollection = cms.InputTag("muons")
)


process.newCombinedSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("initialStepSeeds"), cms.InputTag("pixelPairStepSeeds"), cms.InputTag("mixedTripletStepSeeds"), cms.InputTag("pixelLessStepSeeds"), cms.InputTag("tripletElectronSeeds"), 
        cms.InputTag("pixelPairElectronSeeds"), cms.InputTag("stripPairElectronSeeds"))
)


process.offlineBeamSpot = cms.EDProducer("BeamSpotProducer")


process.photonConvTrajSeedFromSingleLeg = cms.EDProducer("PhotonConversionTrajectorySeedProducerFromSingleLeg",
    vtxMinDoF = cms.double(4),
    beamSpotInputTag = cms.InputTag("offlineBeamSpot"),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        MaxNumberOfPixelClusters = cms.uint32(20000),
        cut = cms.string('strip < 150000 && pixel < 20000 && (strip < 20000 + 7* pixel)'),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters")
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(3.0),
            ptMin = cms.double(0.2),
            originHalfLength = cms.double(12.0),
            beamSpot = cms.InputTag("offlineBeamSpot")
        )
    ),
    DoxcheckSeedCandidates = cms.bool(False),
    xcheckSeedCandidates = cms.string('xcheckSeedCandidates'),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedForPhotonConversion1Leg'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    ),
    TrackRefitter = cms.InputTag("generalTracks"),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(10000),
        SeedingLayers = cms.string('convLayerPairs'),
        maxHitPairsPerTrackAndGenerator = cms.uint32(10)
    ),
    applyTkVtxConstraint = cms.bool(True),
    maxDZSigmas = cms.double(10.0),
    maxNumSelVtx = cms.uint32(2),
    primaryVerticesTag = cms.InputTag("pixelVertices"),
    newSeedCandidates = cms.string('convSeedCandidates')
)


process.pixelLessStepClusters = cms.EDProducer("TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    trajectories = cms.InputTag("mixedTripletStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("mixedTripletStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.pixelLessStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    trajectories = cms.InputTag("pixelLessStepSeeds"),
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.pixelLessStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('pixelLessStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        FilterPixelHits = cms.bool(False),
        FilterStripHits = cms.bool(True),
        FilterAtHelixStage = cms.bool(True)
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(2.0),
            ptMin = cms.double(0.7),
            originHalfLength = cms.double(10.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.pixelLessStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("pixelLessStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(3),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(4),
        chi2n_par = cms.double(0.5),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.3, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.3, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('pixelLessStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(1.3, 4.0),
        d0_par1 = cms.vdouble(1.3, 4.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(4),
            chi2n_par = cms.double(0.35),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelLessStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('pixelLessStepLoose'),
            d0_par2 = cms.vdouble(1.1, 4.0),
            d0_par1 = cms.vdouble(1.1, 4.0),
            res_par = cms.vdouble(0.003, 0.001),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(4),
            chi2n_par = cms.double(0.2),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.9, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.9, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelLessStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.9, 4.0),
            d0_par1 = cms.vdouble(0.9, 4.0),
            preFilterName = cms.string('pixelLessStepTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.pixelLessStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("pixelLessStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    numHitsForSeedCleaner = cms.int32(50),
    TrajectoryBuilder = cms.string('pixelLessStepTrajectoryBuilder')
)


process.pixelLessStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("pixelLessStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter5'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.pixelPairElectronSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('pixelPairElectronSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            useFixedError = cms.bool(True),
            originRadius = cms.double(0.015),
            sigmaZVertex = cms.double(3.0),
            fixedError = cms.double(0.03),
            VertexCollection = cms.InputTag("pixelVertices"),
            ptMin = cms.double(1.0),
            useFoundVertices = cms.bool(True),
            nSigmaZ = cms.double(4.0)
        ),
        ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.pixelPairStepClusters = cms.EDProducer("TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    trajectories = cms.InputTag("lowPtTripletStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("lowPtTripletStepSelector","lowPtTripletStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.pixelPairStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    trajectories = cms.InputTag("pixelPairStepSeeds"),
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.pixelPairStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('pixelPairStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False),
        FilterAtHelixStage = cms.bool(True)
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            useFixedError = cms.bool(True),
            originRadius = cms.double(0.015),
            sigmaZVertex = cms.double(3.0),
            fixedError = cms.double(0.03),
            VertexCollection = cms.InputTag("pixelVertices"),
            ptMin = cms.double(0.6),
            useFoundVertices = cms.bool(True),
            nSigmaZ = cms.double(4.0)
        ),
        ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.pixelPairStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("pixelPairStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(0),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(0.45, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(0.65, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('pixelPairStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.01),
        d0_par2 = cms.vdouble(0.55, 4.0),
        d0_par1 = cms.vdouble(0.55, 4.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelPairStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('pixelPairStepLoose'),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            res_par = cms.vdouble(0.003, 0.01),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.35, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelPairStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            preFilterName = cms.string('pixelPairStepTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.pixelPairStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("pixelPairStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    TrajectoryBuilder = cms.string('pixelPairStepTrajectoryBuilder'),
    numHitsForSeedCleaner = cms.int32(50)
)


process.pixelPairStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("pixelPairStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.refittedStandAloneMuons = cms.EDProducer("StandAloneMuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    InputObjects = cms.InputTag("ancientMuonSeed"),
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(True)
    ),
    STATrajBuilderParameters = cms.PSet(
        DoRefit = cms.bool(True),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            FitDirection = cms.string('insideOut'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
        NavigationType = cms.string('Standard'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            UseSubRecHits = cms.bool(False),
            NMinRecHits = cms.uint32(2),
            RescaleError = cms.double(100.0)
        ),
        DoBackwardFilter = cms.bool(True),
        SeedPosition = cms.string('in'),
        BWFilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            BWSeedType = cms.string('fromGenerator'),
            FitDirection = cms.string('outsideIn'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        RefitterParameters = cms.PSet(
            FitterName = cms.string('KFFitterSmootherSTA'),
            MaxFractionOfLostHits = cms.double(0.05),
            ForceAllIterations = cms.bool(False),
            NumberOfIterations = cms.uint32(3),
            RescaleError = cms.double(100.0)
        )
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive')
)


process.regionalCosmicCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("regionalCosmicTrackerSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilderP5')
)


process.regionalCosmicTrackerSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        MaxNumberOfPixelClusters = cms.uint32(10000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(10000),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        doClusterCheck = cms.bool(False)
    ),
    RegionFactoryPSet = cms.PSet(
        CollectionsPSet = cms.PSet(
            recoMuonsCollection = cms.InputTag(""),
            recoTrackMuonsCollection = cms.InputTag("cosmicMuons"),
            recoL2MuonsCollection = cms.InputTag("")
        ),
        ComponentName = cms.string('CosmicRegionalSeedGenerator'),
        RegionInJetsCheckPSet = cms.PSet(
            recoCaloJetsCollection = cms.InputTag("ak5CaloJets"),
            deltaRExclusionSize = cms.double(0.3),
            jetsPtMin = cms.double(5),
            doJetsExclusionCheck = cms.bool(True)
        ),
        ToolsPSet = cms.PSet(
            regionBase = cms.string('seedOnCosmicMuon'),
            thePropagatorName = cms.string('AnalyticalPropagator')
        ),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            deltaPhiRegion = cms.double(0.1),
            measurementTrackerName = cms.string(''),
            zVertex = cms.double(5),
            deltaEtaRegion = cms.double(0.1),
            ptMin = cms.double(1.0),
            rVertex = cms.double(5)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('CosmicSeedCreator'),
        maxseeds = cms.int32(10000),
        propagator = cms.string('PropagatorWithMaterial')
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('GenericPairGenerator'),
        LayerPSet = cms.PSet(
            TOB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TEC = cms.PSet(
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                minRing = cms.int32(6),
                maxRing = cms.int32(7)
            ),
            layerList = cms.vstring('TOB6+TOB5', 
                'TOB6+TOB4', 
                'TOB6+TOB3', 
                'TOB5+TOB4', 
                'TOB5+TOB3', 
                'TOB4+TOB3', 
                'TEC1_neg+TOB6', 
                'TEC1_neg+TOB5', 
                'TEC1_neg+TOB4', 
                'TEC1_pos+TOB6', 
                'TEC1_pos+TOB5', 
                'TEC1_pos+TOB4')
        )
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    RegionInJetsCheckPSet = cms.PSet(
        doJetsExclusionCheck = cms.bool(False)
    )
)


process.regionalCosmicTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("regionalCosmicCkfTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.roadSearchClouds = cms.EDProducer("RoadSearchCloudMaker",
    MinimalFractionOfUsedLayersPerCloud = cms.double(0.5),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    MergingFraction = cms.double(0.8),
    MaxDetHitsInCloudPerDetId = cms.uint32(8),
    SeedProducer = cms.InputTag("roadSearchSeeds"),
    DoCloudCleaning = cms.bool(True),
    IncreaseMaxNumberOfConsecutiveMissedLayersPerCloud = cms.uint32(4),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    UseStereoRecHits = cms.bool(False),
    ZPhiRoadSize = cms.double(0.06),
    MaximalFractionOfConsecutiveMissedLayersPerCloud = cms.double(0.15),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    MaximalFractionOfMissedLayersPerCloud = cms.double(0.3),
    scalefactorRoadSeedWindow = cms.double(1.5),
    UsePixelsinRS = cms.bool(True),
    IncreaseMaxNumberOfMissedLayersPerCloud = cms.uint32(3),
    RoadsLabel = cms.string(''),
    MaxRecHitsInCloud = cms.int32(100),
    UseRphiRecHits = cms.bool(False),
    StraightLineNoBeamSpotCloud = cms.bool(False),
    RPhiRoadSize = cms.double(0.02),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    MinimumHalfRoad = cms.double(0.55)
)


process.roadSearchCloudsP5 = cms.EDProducer("RoadSearchCloudMaker",
    MinimalFractionOfUsedLayersPerCloud = cms.double(0.3),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    MergingFraction = cms.double(0.8),
    MaxDetHitsInCloudPerDetId = cms.uint32(4),
    SeedProducer = cms.InputTag("roadSearchSeedsP5"),
    DoCloudCleaning = cms.bool(True),
    IncreaseMaxNumberOfConsecutiveMissedLayersPerCloud = cms.uint32(0),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    UseStereoRecHits = cms.bool(True),
    ZPhiRoadSize = cms.double(0.06),
    MaximalFractionOfConsecutiveMissedLayersPerCloud = cms.double(0.35),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    MaximalFractionOfMissedLayersPerCloud = cms.double(0.8),
    scalefactorRoadSeedWindow = cms.double(150),
    UsePixelsinRS = cms.bool(True),
    IncreaseMaxNumberOfMissedLayersPerCloud = cms.uint32(0),
    RoadsLabel = cms.string('P5'),
    MaxRecHitsInCloud = cms.int32(100),
    UseRphiRecHits = cms.bool(True),
    StraightLineNoBeamSpotCloud = cms.bool(True),
    RPhiRoadSize = cms.double(5.0),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    MinimumHalfRoad = cms.double(3.3)
)


process.roadSearchCloudsP5Bottom = cms.EDProducer("RoadSearchCloudMaker",
    MinimalFractionOfUsedLayersPerCloud = cms.double(0.3),
    pixelRecHits = cms.InputTag("siPixelRecHitsBottom"),
    MergingFraction = cms.double(0.8),
    MaxDetHitsInCloudPerDetId = cms.uint32(4),
    SeedProducer = cms.InputTag("roadSearchSeedsP5Bottom"),
    DoCloudCleaning = cms.bool(True),
    IncreaseMaxNumberOfConsecutiveMissedLayersPerCloud = cms.uint32(0),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    UseStereoRecHits = cms.bool(True),
    ZPhiRoadSize = cms.double(0.06),
    MaximalFractionOfConsecutiveMissedLayersPerCloud = cms.double(0.35),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit"),
    MaximalFractionOfMissedLayersPerCloud = cms.double(0.8),
    scalefactorRoadSeedWindow = cms.double(150),
    UsePixelsinRS = cms.bool(True),
    IncreaseMaxNumberOfMissedLayersPerCloud = cms.uint32(0),
    RoadsLabel = cms.string('P5'),
    MaxRecHitsInCloud = cms.int32(100),
    UseRphiRecHits = cms.bool(True),
    StraightLineNoBeamSpotCloud = cms.bool(True),
    RPhiRoadSize = cms.double(5.0),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
    MinimumHalfRoad = cms.double(3.3),
    ClusterCollectionLabel = cms.InputTag("siStripClustersBottom")
)


process.roadSearchCloudsP5Top = cms.EDProducer("RoadSearchCloudMaker",
    MinimalFractionOfUsedLayersPerCloud = cms.double(0.3),
    pixelRecHits = cms.InputTag("siPixelRecHitsTop"),
    MergingFraction = cms.double(0.8),
    MaxDetHitsInCloudPerDetId = cms.uint32(4),
    SeedProducer = cms.InputTag("roadSearchSeedsP5Top"),
    DoCloudCleaning = cms.bool(True),
    IncreaseMaxNumberOfConsecutiveMissedLayersPerCloud = cms.uint32(0),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    UseStereoRecHits = cms.bool(True),
    ZPhiRoadSize = cms.double(0.06),
    MaximalFractionOfConsecutiveMissedLayersPerCloud = cms.double(0.35),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    MaximalFractionOfMissedLayersPerCloud = cms.double(0.8),
    scalefactorRoadSeedWindow = cms.double(150),
    UsePixelsinRS = cms.bool(True),
    IncreaseMaxNumberOfMissedLayersPerCloud = cms.uint32(0),
    RoadsLabel = cms.string('P5'),
    MaxRecHitsInCloud = cms.int32(100),
    UseRphiRecHits = cms.bool(True),
    StraightLineNoBeamSpotCloud = cms.bool(True),
    RPhiRoadSize = cms.double(5.0),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
    MinimumHalfRoad = cms.double(3.3),
    ClusterCollectionLabel = cms.InputTag("siStripClustersTop")
)


process.roadSearchSeeds = cms.EDProducer("RoadSearchSeedFinder",
    OuterSeedRecHitAccessMode = cms.string('RPHI'),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    MaximalEndcapImpactParameter = cms.double(1.2),
    MergeSeedsCenterCut_C = cms.double(0.4),
    MergeSeedsCenterCut_B = cms.double(0.25),
    MergeSeedsCenterCut_A = cms.double(0.05),
    MergeSeedsDifferentHitsCut = cms.uint32(1),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    MaximalBarrelImpactParameter = cms.double(0.2),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfSeeds = cms.int32(-1),
    doClusterCheck = cms.bool(False),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    OuterSeedRecHitAccessUseStereo = cms.bool(False),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    MinimalReconstructedTransverseMomentum = cms.double(1.5),
    PhiRangeForDetIdLookupInRings = cms.double(0.5),
    Mode = cms.string('STANDARD'),
    MaxNumberOfPixelClusters = cms.uint32(300),
    AllNegativeOnly = cms.bool(False),
    RoadsLabel = cms.string(''),
    InnerSeedRecHitAccessMode = cms.string('RPHI'),
    InnerSeedRecHitAccessUseStereo = cms.bool(False),
    OuterSeedRecHitAccessUseRPhi = cms.bool(False),
    MergeSeedsRadiusCut_B = cms.double(0.25),
    MergeSeedsRadiusCut_C = cms.double(0.4),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    MergeSeedsRadiusCut_A = cms.double(0.05),
    InnerSeedRecHitAccessUseRPhi = cms.bool(False),
    AllPositiveOnly = cms.bool(False)
)


process.roadSearchSeedsP5 = cms.EDProducer("RoadSearchSeedFinder",
    OuterSeedRecHitAccessMode = cms.string('STANDARD'),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    MaximalEndcapImpactParameter = cms.double(1.2),
    MergeSeedsCenterCut_C = cms.double(0.4),
    MergeSeedsCenterCut_B = cms.double(0.25),
    MergeSeedsCenterCut_A = cms.double(0.05),
    MergeSeedsDifferentHitsCut = cms.uint32(1),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    MaximalBarrelImpactParameter = cms.double(0.2),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfSeeds = cms.int32(1000),
    doClusterCheck = cms.bool(True),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    OuterSeedRecHitAccessUseStereo = cms.bool(True),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    MinimalReconstructedTransverseMomentum = cms.double(1.5),
    PhiRangeForDetIdLookupInRings = cms.double(0.5),
    Mode = cms.string('STRAIGHT-LINE'),
    MaxNumberOfPixelClusters = cms.uint32(300),
    AllNegativeOnly = cms.bool(False),
    RoadsLabel = cms.string('P5'),
    InnerSeedRecHitAccessMode = cms.string('STANDARD'),
    InnerSeedRecHitAccessUseStereo = cms.bool(True),
    OuterSeedRecHitAccessUseRPhi = cms.bool(True),
    MergeSeedsRadiusCut_B = cms.double(0.25),
    MergeSeedsRadiusCut_C = cms.double(0.4),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    MergeSeedsRadiusCut_A = cms.double(0.05),
    InnerSeedRecHitAccessUseRPhi = cms.bool(True),
    AllPositiveOnly = cms.bool(False)
)


process.roadSearchSeedsP5Bottom = cms.EDProducer("RoadSearchSeedFinder",
    OuterSeedRecHitAccessMode = cms.string('STANDARD'),
    pixelRecHits = cms.InputTag("siPixelRecHitsBottom"),
    MaximalEndcapImpactParameter = cms.double(1.2),
    MergeSeedsCenterCut_C = cms.double(0.4),
    MergeSeedsCenterCut_B = cms.double(0.25),
    MergeSeedsCenterCut_A = cms.double(0.05),
    MergeSeedsDifferentHitsCut = cms.uint32(1),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    MaximalBarrelImpactParameter = cms.double(0.2),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfSeeds = cms.int32(1000),
    doClusterCheck = cms.bool(True),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit"),
    ClusterCollectionLabel = cms.InputTag("siStripClustersBottom"),
    OuterSeedRecHitAccessUseStereo = cms.bool(True),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    MinimalReconstructedTransverseMomentum = cms.double(1.5),
    PhiRangeForDetIdLookupInRings = cms.double(0.5),
    Mode = cms.string('STRAIGHT-LINE'),
    MaxNumberOfPixelClusters = cms.uint32(300),
    AllNegativeOnly = cms.bool(True),
    RoadsLabel = cms.string('P5'),
    InnerSeedRecHitAccessMode = cms.string('STANDARD'),
    InnerSeedRecHitAccessUseStereo = cms.bool(True),
    OuterSeedRecHitAccessUseRPhi = cms.bool(True),
    MergeSeedsRadiusCut_B = cms.double(0.25),
    MergeSeedsRadiusCut_C = cms.double(0.4),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
    MergeSeedsRadiusCut_A = cms.double(0.05),
    InnerSeedRecHitAccessUseRPhi = cms.bool(True),
    AllPositiveOnly = cms.bool(False)
)


process.roadSearchSeedsP5Top = cms.EDProducer("RoadSearchSeedFinder",
    OuterSeedRecHitAccessMode = cms.string('STANDARD'),
    pixelRecHits = cms.InputTag("siPixelRecHitsTop"),
    MaximalEndcapImpactParameter = cms.double(1.2),
    MergeSeedsCenterCut_C = cms.double(0.4),
    MergeSeedsCenterCut_B = cms.double(0.25),
    MergeSeedsCenterCut_A = cms.double(0.05),
    MergeSeedsDifferentHitsCut = cms.uint32(1),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    MaximalBarrelImpactParameter = cms.double(0.2),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfSeeds = cms.int32(1000),
    doClusterCheck = cms.bool(True),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    ClusterCollectionLabel = cms.InputTag("siStripClustersTop"),
    OuterSeedRecHitAccessUseStereo = cms.bool(True),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    MinimalReconstructedTransverseMomentum = cms.double(1.5),
    PhiRangeForDetIdLookupInRings = cms.double(0.5),
    Mode = cms.string('STRAIGHT-LINE'),
    MaxNumberOfPixelClusters = cms.uint32(300),
    AllNegativeOnly = cms.bool(False),
    RoadsLabel = cms.string('P5'),
    InnerSeedRecHitAccessMode = cms.string('STANDARD'),
    InnerSeedRecHitAccessUseStereo = cms.bool(True),
    OuterSeedRecHitAccessUseRPhi = cms.bool(True),
    MergeSeedsRadiusCut_B = cms.double(0.25),
    MergeSeedsRadiusCut_C = cms.double(0.4),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
    MergeSeedsRadiusCut_A = cms.double(0.05),
    InnerSeedRecHitAccessUseRPhi = cms.bool(True),
    AllPositiveOnly = cms.bool(True)
)


process.rsTrackCandidates = cms.EDProducer("RoadSearchTrackCandidateMaker",
    NumHitCut = cms.int32(5),
    InitialVertexErrorXY = cms.double(0.2),
    HitChi2Cut = cms.double(30.0),
    StraightLineNoBeamSpotCloud = cms.bool(False),
    nFoundMin = cms.int32(4),
    MinimumChunkLength = cms.int32(7),
    TTRHBuilder = cms.string('WithTrackAngle'),
    CosmicTrackMerging = cms.bool(False),
    MeasurementTrackerName = cms.string(''),
    CloudProducer = cms.InputTag("roadSearchClouds"),
    CosmicSeedPt = cms.double(5.0),
    SplitMatchedHits = cms.bool(False)
)


process.rsTrackCandidatesP5 = cms.EDProducer("RoadSearchTrackCandidateMaker",
    NumHitCut = cms.int32(4),
    InitialVertexErrorXY = cms.double(0.2),
    HitChi2Cut = cms.double(30.0),
    StraightLineNoBeamSpotCloud = cms.bool(True),
    nFoundMin = cms.int32(2),
    MinimumChunkLength = cms.int32(2),
    TTRHBuilder = cms.string('WithTrackAngle'),
    CosmicTrackMerging = cms.bool(True),
    MeasurementTrackerName = cms.string(''),
    CloudProducer = cms.InputTag("roadSearchCloudsP5"),
    CosmicSeedPt = cms.double(5.0),
    SplitMatchedHits = cms.bool(True)
)


process.rsTrackCandidatesP5Bottom = cms.EDProducer("RoadSearchTrackCandidateMaker",
    NumHitCut = cms.int32(4),
    InitialVertexErrorXY = cms.double(0.2),
    HitChi2Cut = cms.double(30.0),
    StraightLineNoBeamSpotCloud = cms.bool(True),
    nFoundMin = cms.int32(2),
    MinimumChunkLength = cms.int32(2),
    TTRHBuilder = cms.string('WithTrackAngle'),
    CosmicTrackMerging = cms.bool(True),
    MeasurementTrackerName = cms.string(''),
    CloudProducer = cms.InputTag("roadSearchCloudsP5Bottom"),
    CosmicSeedPt = cms.double(5.0),
    SplitMatchedHits = cms.bool(True)
)


process.rsTrackCandidatesP5Top = cms.EDProducer("RoadSearchTrackCandidateMaker",
    NumHitCut = cms.int32(4),
    InitialVertexErrorXY = cms.double(0.2),
    HitChi2Cut = cms.double(30.0),
    StraightLineNoBeamSpotCloud = cms.bool(True),
    nFoundMin = cms.int32(2),
    MinimumChunkLength = cms.int32(2),
    TTRHBuilder = cms.string('WithTrackAngle'),
    CosmicTrackMerging = cms.bool(True),
    MeasurementTrackerName = cms.string(''),
    CloudProducer = cms.InputTag("roadSearchCloudsP5Top"),
    CosmicSeedPt = cms.double(5.0),
    SplitMatchedHits = cms.bool(True)
)


process.rsWithMaterialTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("rsTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('rs'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.rsWithMaterialTracksCosmics = cms.EDProducer("TrackProducer",
    src = cms.InputTag("rsTrackCandidatesP5"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('rs'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.rsWithMaterialTracksP5 = cms.EDProducer("CosmicTrackSelector",
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    minNumber3DLayers = cms.uint32(0),
    src = cms.InputTag("rsWithMaterialTracksCosmics"),
    copyExtras = cms.untracked.bool(True),
    min_pt = cms.double(1.0),
    copyTrajectories = cms.untracked.bool(True),
    qualityBit = cms.string(''),
    minNumberLayers = cms.uint32(0),
    chi2n_par = cms.double(10.0),
    max_eta = cms.double(2.0),
    min_nPixelHit = cms.uint32(0),
    min_nHit = cms.uint32(5),
    max_z0 = cms.double(300.0),
    beamspot = cms.InputTag("offlineBeamSpot")
)


process.rsWithMaterialTracksP5Bottom = cms.EDProducer("TrackProducer",
    src = cms.InputTag("rsTrackCandidatesP5Bottom"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerBottom"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('rs'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.rsWithMaterialTracksP5Top = cms.EDProducer("TrackProducer",
    src = cms.InputTag("rsTrackCandidatesP5Top"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerTop"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('rs'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.seedClusterRemover = cms.EDProducer("SeedClusterRemover",
    trajectories = cms.InputTag("initialStepSeeds"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.siPixelClusters = cms.EDProducer("SiPixelClusterProducer",
    src = cms.InputTag("siPixelDigis"),
    ChannelThreshold = cms.int32(1000),
    maxNumberOfClusters = cms.int32(-1),
    SplitClusters = cms.bool(False),
    MissCalibrate = cms.untracked.bool(True),
    VCaltoElectronGain = cms.int32(65),
    VCaltoElectronOffset = cms.int32(-414),
    payloadType = cms.string('Offline'),
    SeedThreshold = cms.int32(1000),
    ClusterThreshold = cms.double(4000.0)
)


process.siPixelClustersBottom = cms.EDProducer("PixelClusterSelectorTopBottom",
    y = cms.double(-1),
    label = cms.InputTag("siPixelClusters")
)


process.siPixelClustersTop = cms.EDProducer("PixelClusterSelectorTopBottom",
    y = cms.double(1),
    label = cms.InputTag("siPixelClusters")
)


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClusters"),
    CPE = cms.string('PixelCPEGeneric')
)


process.siPixelRecHitsBottom = cms.EDProducer("SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersBottom"),
    CPE = cms.string('PixelCPEGeneric')
)


process.siPixelRecHitsTop = cms.EDProducer("SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersTop"),
    CPE = cms.string('PixelCPEGeneric')
)


process.siStripClusters = cms.EDProducer("SiStripClusterizer",
    DigiProducersList = cms.VInputTag(cms.InputTag("siStripDigis","ZeroSuppressed"), cms.InputTag("siStripZeroSuppression","VirginRaw"), cms.InputTag("siStripZeroSuppression","ProcessedRaw"), cms.InputTag("siStripZeroSuppression","ScopeMode")),
    Clusterizer = cms.PSet(
        ChannelThreshold = cms.double(2.0),
        MaxSequentialBad = cms.uint32(1),
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        MaxSequentialHoles = cms.uint32(0),
        MaxAdjacentBad = cms.uint32(0),
        QualityLabel = cms.string(''),
        SeedThreshold = cms.double(3.0),
        RemoveApvShots = cms.bool(True),
        ClusterThreshold = cms.double(5.0)
    )
)


process.siStripClustersBottom = cms.EDProducer("StripClusterSelectorTopBottom",
    y = cms.double(-1),
    label = cms.InputTag("siStripClusters")
)


process.siStripClustersTop = cms.EDProducer("StripClusterSelectorTopBottom",
    y = cms.double(1),
    label = cms.InputTag("siStripClusters")
)


process.siStripMatchedRecHits = cms.EDProducer("SiStripRecHitConverter",
    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
    Regional = cms.bool(False),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False),
    matchedRecHits = cms.string('matchedRecHit'),
    LazyGetterProducer = cms.InputTag("SiStripRawToClustersFacility"),
    ClusterProducer = cms.InputTag("siStripClusters"),
    VerbosityLevel = cms.untracked.int32(1),
    rphiRecHits = cms.string('rphiRecHit'),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    siStripQualityLabel = cms.ESInputTag(""),
    MaskBadAPVFibers = cms.bool(False)
)


process.siStripMatchedRecHitsBottom = cms.EDProducer("SiStripRecHitConverter",
    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
    LazyGetterProducer = cms.InputTag("SiStripRawToClustersFacility"),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False),
    matchedRecHits = cms.string('matchedRecHit'),
    Regional = cms.bool(False),
    ClusterProducer = cms.InputTag("siStripClustersBottom"),
    VerbosityLevel = cms.untracked.int32(1),
    rphiRecHits = cms.string('rphiRecHit'),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    siStripQualityLabel = cms.ESInputTag(""),
    MaskBadAPVFibers = cms.bool(False)
)


process.siStripMatchedRecHitsTop = cms.EDProducer("SiStripRecHitConverter",
    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
    LazyGetterProducer = cms.InputTag("SiStripRawToClustersFacility"),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False),
    matchedRecHits = cms.string('matchedRecHit'),
    Regional = cms.bool(False),
    ClusterProducer = cms.InputTag("siStripClustersTop"),
    VerbosityLevel = cms.untracked.int32(1),
    rphiRecHits = cms.string('rphiRecHit'),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    siStripQualityLabel = cms.ESInputTag(""),
    MaskBadAPVFibers = cms.bool(False)
)


process.siStripZeroSuppression = cms.EDProducer("SiStripZeroSuppression",
    fixCM = cms.bool(False),
    DigisToMergeVR = cms.InputTag("siStripVRDigis","VirginRaw"),
    produceCalculatedBaseline = cms.bool(False),
    produceRawDigis = cms.bool(True),
    RawDigiProducersList = cms.VInputTag(cms.InputTag("siStripDigis","VirginRaw"), cms.InputTag("siStripDigis","ProcessedRaw"), cms.InputTag("siStripDigis","ScopeMode")),
    storeInZScollBadAPV = cms.bool(True),
    mergeCollections = cms.bool(False),
    Algorithms = cms.PSet(
        CutToAvoidSignal = cms.double(2.0),
        slopeY = cms.int32(4),
        slopeX = cms.int32(3),
        PedestalSubtractionFedMode = cms.bool(False),
        Fraction = cms.double(0.2),
        minStripsToFit = cms.uint32(4),
        consecThreshold = cms.uint32(5),
        hitStripThreshold = cms.uint32(40),
        Deviation = cms.uint32(25),
        CommonModeNoiseSubtractionMode = cms.string('IteratedMedian'),
        filteredBaselineDerivativeSumSquare = cms.double(30),
        ApplyBaselineCleaner = cms.bool(True),
        doAPVRestore = cms.bool(True),
        TruncateInSuppressor = cms.bool(True),
        restoreThreshold = cms.double(0.5),
        APVInspectMode = cms.string('BaselineFollower'),
        ForceNoRestore = cms.bool(False),
        useRealMeanCM = cms.bool(False),
        ApplyBaselineRejection = cms.bool(True),
        DeltaCMThreshold = cms.uint32(20),
        nSigmaNoiseDerTh = cms.uint32(4),
        nSaturatedStrip = cms.uint32(2),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        useCMMeanMap = cms.bool(False),
        SelfSelectRestoreAlgo = cms.bool(False),
        distortionThreshold = cms.uint32(20),
        filteredBaselineMax = cms.double(6),
        Iterations = cms.int32(3),
        CleaningSequence = cms.uint32(1),
        nSmooth = cms.uint32(9),
        APVRestoreMode = cms.string('BaselineFollower'),
        MeanCM = cms.int32(0)
    ),
    DigisToMergeZS = cms.InputTag("siStripDigis","ZeroSuppressed"),
    storeCM = cms.bool(True),
    produceBaselinePoints = cms.bool(False)
)


process.simpleCosmicBONSeeds = cms.EDProducer("SimpleCosmicBONSeeder",
    helixDebugLevel = cms.untracked.uint32(0),
    seedOnMiddle = cms.bool(False),
    RegionPSet = cms.PSet(
        pMin = cms.double(1.0),
        originRadius = cms.double(150.0),
        ptMin = cms.double(0.5),
        originZPosition = cms.double(0.0),
        originHalfLength = cms.double(90.0)
    ),
    ClusterCheckPSet = cms.PSet(
        MaxNumberOfPixelClusters = cms.uint32(300),
        DontCountDetsAboveNClusters = cms.uint32(20),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(300),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters")
    ),
    HitsPerModuleCheck = cms.PSet(
        checkHitsPerModule = cms.bool(True),
        Thresholds = cms.PSet(
            TOB = cms.int32(20),
            TID = cms.int32(20),
            TEC = cms.int32(20),
            TIB = cms.int32(20)
        )
    ),
    minimumGoodHitsInSeed = cms.int32(3),
    NegativeYOnly = cms.bool(False),
    maxTriplets = cms.int32(50000),
    TripletsPSet = cms.PSet(
        TOB5 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
        ),
        TOB4 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
        ),
        TIB1 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TOB6 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
        ),
        TOB1 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TOB3 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
        ),
        TOB2 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TEC = cms.PSet(
            useSimpleRphiHitsCleaner = cms.bool(False),
            minRing = cms.int32(5),
            matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
            useRingSlector = cms.bool(False),
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
            maxRing = cms.int32(7)
        ),
        TIB2 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TIB3 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
        ),
        layerList = cms.vstring('TOB4+TOB5+TOB6', 
            'TOB3+TOB5+TOB6', 
            'TOB3+TOB4+TOB5', 
            'TOB3+TOB4+TOB6', 
            'TOB2+TOB4+TOB5', 
            'TOB2+TOB3+TOB5', 
            'TEC7_pos+TEC8_pos+TEC9_pos', 
            'TEC6_pos+TEC7_pos+TEC8_pos', 
            'TEC5_pos+TEC6_pos+TEC7_pos', 
            'TEC4_pos+TEC5_pos+TEC6_pos', 
            'TEC3_pos+TEC4_pos+TEC5_pos', 
            'TEC2_pos+TEC3_pos+TEC4_pos', 
            'TEC1_pos+TEC2_pos+TEC3_pos', 
            'TEC7_neg+TEC8_neg+TEC9_neg', 
            'TEC6_neg+TEC7_neg+TEC8_neg', 
            'TEC5_neg+TEC6_neg+TEC7_neg', 
            'TEC4_neg+TEC5_neg+TEC6_neg', 
            'TEC3_neg+TEC4_neg+TEC5_neg', 
            'TEC2_neg+TEC3_neg+TEC4_neg', 
            'TEC1_neg+TEC2_neg+TEC3_neg', 
            'TEC6_pos+TEC8_pos+TEC9_pos', 
            'TEC5_pos+TEC7_pos+TEC8_pos', 
            'TEC4_pos+TEC6_pos+TEC7_pos', 
            'TEC3_pos+TEC5_pos+TEC6_pos', 
            'TEC2_pos+TEC4_pos+TEC5_pos', 
            'TEC1_pos+TEC3_pos+TEC4_pos', 
            'TEC6_pos+TEC7_pos+TEC9_pos', 
            'TEC5_pos+TEC6_pos+TEC8_pos', 
            'TEC4_pos+TEC5_pos+TEC7_pos', 
            'TEC3_pos+TEC4_pos+TEC6_pos', 
            'TEC2_pos+TEC3_pos+TEC5_pos', 
            'TEC1_pos+TEC2_pos+TEC4_pos', 
            'TEC6_neg+TEC8_neg+TEC9_neg', 
            'TEC5_neg+TEC7_neg+TEC8_neg', 
            'TEC4_neg+TEC6_neg+TEC7_neg', 
            'TEC3_neg+TEC5_neg+TEC6_neg', 
            'TEC2_neg+TEC4_neg+TEC5_neg', 
            'TEC1_neg+TEC3_neg+TEC4_neg', 
            'TEC6_neg+TEC7_neg+TEC9_neg', 
            'TEC5_neg+TEC6_neg+TEC8_neg', 
            'TEC4_neg+TEC5_neg+TEC7_neg', 
            'TEC3_neg+TEC4_neg+TEC6_neg', 
            'TEC2_neg+TEC3_neg+TEC5_neg', 
            'TEC1_neg+TEC2_neg+TEC4_neg', 
            'TOB6+TEC1_pos+TEC2_pos', 
            'TOB6+TEC1_neg+TEC2_neg', 
            'TOB6+TOB5+TEC1_pos', 
            'TOB6+TOB5+TEC1_neg'),
        debugLevel = cms.untracked.uint32(0)
    ),
    seedDebugLevel = cms.untracked.uint32(0),
    PositiveYOnly = cms.bool(False),
    writeTriplets = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    ClusterChargeCheck = cms.PSet(
        Thresholds = cms.PSet(
            TOB = cms.int32(0),
            TID = cms.int32(0),
            TEC = cms.int32(0),
            TIB = cms.int32(0)
        ),
        matchedRecHitsUseAnd = cms.bool(True),
        checkCharge = cms.bool(False)
    ),
    maxSeeds = cms.int32(20000),
    rescaleError = cms.double(1.0)
)


process.simpleCosmicBONSeedsBottom = cms.EDProducer("SimpleCosmicBONSeeder",
    helixDebugLevel = cms.untracked.uint32(0),
    seedOnMiddle = cms.bool(False),
    RegionPSet = cms.PSet(
        pMin = cms.double(1.0),
        originRadius = cms.double(150.0),
        ptMin = cms.double(0.5),
        originZPosition = cms.double(0.0),
        originHalfLength = cms.double(90.0)
    ),
    ClusterCheckPSet = cms.PSet(
        MaxNumberOfPixelClusters = cms.uint32(300),
        DontCountDetsAboveNClusters = cms.uint32(20),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClustersBottom")
    ),
    HitsPerModuleCheck = cms.PSet(
        checkHitsPerModule = cms.bool(True),
        Thresholds = cms.PSet(
            TOB = cms.int32(20),
            TID = cms.int32(20),
            TEC = cms.int32(20),
            TIB = cms.int32(20)
        )
    ),
    minimumGoodHitsInSeed = cms.int32(3),
    NegativeYOnly = cms.bool(True),
    maxTriplets = cms.int32(50000),
    TripletsPSet = cms.PSet(
        TOB5 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
        ),
        TOB4 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
        ),
        TIB1 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TOB6 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
        ),
        TOB1 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TOB3 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
        ),
        TOB2 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TEC = cms.PSet(
            useSimpleRphiHitsCleaner = cms.bool(False),
            minRing = cms.int32(5),
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
            useRingSlector = cms.bool(False),
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
            maxRing = cms.int32(7)
        ),
        TIB2 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TIB3 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
        ),
        layerList = cms.vstring('TOB4+TOB5+TOB6', 
            'TOB3+TOB5+TOB6', 
            'TOB3+TOB4+TOB5', 
            'TOB3+TOB4+TOB6', 
            'TOB2+TOB4+TOB5', 
            'TOB2+TOB3+TOB5', 
            'TEC7_pos+TEC8_pos+TEC9_pos', 
            'TEC6_pos+TEC7_pos+TEC8_pos', 
            'TEC5_pos+TEC6_pos+TEC7_pos', 
            'TEC4_pos+TEC5_pos+TEC6_pos', 
            'TEC3_pos+TEC4_pos+TEC5_pos', 
            'TEC2_pos+TEC3_pos+TEC4_pos', 
            'TEC1_pos+TEC2_pos+TEC3_pos', 
            'TEC7_neg+TEC8_neg+TEC9_neg', 
            'TEC6_neg+TEC7_neg+TEC8_neg', 
            'TEC5_neg+TEC6_neg+TEC7_neg', 
            'TEC4_neg+TEC5_neg+TEC6_neg', 
            'TEC3_neg+TEC4_neg+TEC5_neg', 
            'TEC2_neg+TEC3_neg+TEC4_neg', 
            'TEC1_neg+TEC2_neg+TEC3_neg', 
            'TEC6_pos+TEC8_pos+TEC9_pos', 
            'TEC5_pos+TEC7_pos+TEC8_pos', 
            'TEC4_pos+TEC6_pos+TEC7_pos', 
            'TEC3_pos+TEC5_pos+TEC6_pos', 
            'TEC2_pos+TEC4_pos+TEC5_pos', 
            'TEC1_pos+TEC3_pos+TEC4_pos', 
            'TEC6_pos+TEC7_pos+TEC9_pos', 
            'TEC5_pos+TEC6_pos+TEC8_pos', 
            'TEC4_pos+TEC5_pos+TEC7_pos', 
            'TEC3_pos+TEC4_pos+TEC6_pos', 
            'TEC2_pos+TEC3_pos+TEC5_pos', 
            'TEC1_pos+TEC2_pos+TEC4_pos', 
            'TEC6_neg+TEC8_neg+TEC9_neg', 
            'TEC5_neg+TEC7_neg+TEC8_neg', 
            'TEC4_neg+TEC6_neg+TEC7_neg', 
            'TEC3_neg+TEC5_neg+TEC6_neg', 
            'TEC2_neg+TEC4_neg+TEC5_neg', 
            'TEC1_neg+TEC3_neg+TEC4_neg', 
            'TEC6_neg+TEC7_neg+TEC9_neg', 
            'TEC5_neg+TEC6_neg+TEC8_neg', 
            'TEC4_neg+TEC5_neg+TEC7_neg', 
            'TEC3_neg+TEC4_neg+TEC6_neg', 
            'TEC2_neg+TEC3_neg+TEC5_neg', 
            'TEC1_neg+TEC2_neg+TEC4_neg', 
            'TOB6+TEC1_pos+TEC2_pos', 
            'TOB6+TEC1_neg+TEC2_neg', 
            'TOB6+TOB5+TEC1_pos', 
            'TOB6+TOB5+TEC1_neg'),
        debugLevel = cms.untracked.uint32(0)
    ),
    seedDebugLevel = cms.untracked.uint32(0),
    PositiveYOnly = cms.bool(False),
    writeTriplets = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    ClusterChargeCheck = cms.PSet(
        Thresholds = cms.PSet(
            TOB = cms.int32(0),
            TID = cms.int32(0),
            TEC = cms.int32(0),
            TIB = cms.int32(0)
        ),
        matchedRecHitsUseAnd = cms.bool(True),
        checkCharge = cms.bool(False)
    ),
    maxSeeds = cms.int32(20000),
    rescaleError = cms.double(1.0)
)


process.simpleCosmicBONSeedsTop = cms.EDProducer("SimpleCosmicBONSeeder",
    helixDebugLevel = cms.untracked.uint32(0),
    seedOnMiddle = cms.bool(False),
    RegionPSet = cms.PSet(
        pMin = cms.double(1.0),
        originRadius = cms.double(150.0),
        ptMin = cms.double(0.5),
        originZPosition = cms.double(0.0),
        originHalfLength = cms.double(90.0)
    ),
    ClusterCheckPSet = cms.PSet(
        MaxNumberOfPixelClusters = cms.uint32(300),
        DontCountDetsAboveNClusters = cms.uint32(20),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClustersTop")
    ),
    HitsPerModuleCheck = cms.PSet(
        checkHitsPerModule = cms.bool(True),
        Thresholds = cms.PSet(
            TOB = cms.int32(20),
            TID = cms.int32(20),
            TEC = cms.int32(20),
            TIB = cms.int32(20)
        )
    ),
    minimumGoodHitsInSeed = cms.int32(3),
    NegativeYOnly = cms.bool(False),
    maxTriplets = cms.int32(50000),
    TripletsPSet = cms.PSet(
        TOB5 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
        ),
        TOB4 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
        ),
        TIB1 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TOB6 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
        ),
        TOB1 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TOB3 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
        ),
        TOB2 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TEC = cms.PSet(
            useSimpleRphiHitsCleaner = cms.bool(False),
            minRing = cms.int32(5),
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
            useRingSlector = cms.bool(False),
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
            maxRing = cms.int32(7)
        ),
        TIB2 = cms.PSet(
            matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
            TTRHBuilder = cms.string('WithTrackAngle')
        ),
        TIB3 = cms.PSet(
            TTRHBuilder = cms.string('WithTrackAngle'),
            rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
        ),
        layerList = cms.vstring('TOB4+TOB5+TOB6', 
            'TOB3+TOB5+TOB6', 
            'TOB3+TOB4+TOB5', 
            'TOB3+TOB4+TOB6', 
            'TOB2+TOB4+TOB5', 
            'TOB2+TOB3+TOB5', 
            'TEC7_pos+TEC8_pos+TEC9_pos', 
            'TEC6_pos+TEC7_pos+TEC8_pos', 
            'TEC5_pos+TEC6_pos+TEC7_pos', 
            'TEC4_pos+TEC5_pos+TEC6_pos', 
            'TEC3_pos+TEC4_pos+TEC5_pos', 
            'TEC2_pos+TEC3_pos+TEC4_pos', 
            'TEC1_pos+TEC2_pos+TEC3_pos', 
            'TEC7_neg+TEC8_neg+TEC9_neg', 
            'TEC6_neg+TEC7_neg+TEC8_neg', 
            'TEC5_neg+TEC6_neg+TEC7_neg', 
            'TEC4_neg+TEC5_neg+TEC6_neg', 
            'TEC3_neg+TEC4_neg+TEC5_neg', 
            'TEC2_neg+TEC3_neg+TEC4_neg', 
            'TEC1_neg+TEC2_neg+TEC3_neg', 
            'TEC6_pos+TEC8_pos+TEC9_pos', 
            'TEC5_pos+TEC7_pos+TEC8_pos', 
            'TEC4_pos+TEC6_pos+TEC7_pos', 
            'TEC3_pos+TEC5_pos+TEC6_pos', 
            'TEC2_pos+TEC4_pos+TEC5_pos', 
            'TEC1_pos+TEC3_pos+TEC4_pos', 
            'TEC6_pos+TEC7_pos+TEC9_pos', 
            'TEC5_pos+TEC6_pos+TEC8_pos', 
            'TEC4_pos+TEC5_pos+TEC7_pos', 
            'TEC3_pos+TEC4_pos+TEC6_pos', 
            'TEC2_pos+TEC3_pos+TEC5_pos', 
            'TEC1_pos+TEC2_pos+TEC4_pos', 
            'TEC6_neg+TEC8_neg+TEC9_neg', 
            'TEC5_neg+TEC7_neg+TEC8_neg', 
            'TEC4_neg+TEC6_neg+TEC7_neg', 
            'TEC3_neg+TEC5_neg+TEC6_neg', 
            'TEC2_neg+TEC4_neg+TEC5_neg', 
            'TEC1_neg+TEC3_neg+TEC4_neg', 
            'TEC6_neg+TEC7_neg+TEC9_neg', 
            'TEC5_neg+TEC6_neg+TEC8_neg', 
            'TEC4_neg+TEC5_neg+TEC7_neg', 
            'TEC3_neg+TEC4_neg+TEC6_neg', 
            'TEC2_neg+TEC3_neg+TEC5_neg', 
            'TEC1_neg+TEC2_neg+TEC4_neg', 
            'TOB6+TEC1_pos+TEC2_pos', 
            'TOB6+TEC1_neg+TEC2_neg', 
            'TOB6+TOB5+TEC1_pos', 
            'TOB6+TOB5+TEC1_neg'),
        debugLevel = cms.untracked.uint32(0)
    ),
    seedDebugLevel = cms.untracked.uint32(0),
    PositiveYOnly = cms.bool(True),
    writeTriplets = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    ClusterChargeCheck = cms.PSet(
        Thresholds = cms.PSet(
            TOB = cms.int32(0),
            TID = cms.int32(0),
            TEC = cms.int32(0),
            TIB = cms.int32(0)
        ),
        matchedRecHitsUseAnd = cms.bool(True),
        checkCharge = cms.bool(False)
    ),
    maxSeeds = cms.int32(20000),
    rescaleError = cms.double(1.0)
)


process.splittedTracksP5 = cms.EDProducer("TrackProducer",
    src = cms.InputTag("cosmicTrackSplitter"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('cosmic'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.standAloneMuons = cms.EDProducer("StandAloneMuonProducer",
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(True)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    InputObjects = cms.InputTag("ancientMuonSeed"),
    MuonTrajectoryBuilder = cms.string('Exhaustive'),
    STATrajBuilderParameters = cms.PSet(
        DoRefit = cms.bool(False),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            FitDirection = cms.string('insideOut'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        SeedPropagator = cms.string('SteppingHelixPropagatorAny'),
        NavigationType = cms.string('Standard'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            UseSubRecHits = cms.bool(False),
            NMinRecHits = cms.uint32(2),
            RescaleError = cms.double(100.0)
        ),
        DoBackwardFilter = cms.bool(True),
        SeedPosition = cms.string('in'),
        BWFilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            BWSeedType = cms.string('fromGenerator'),
            FitDirection = cms.string('outsideIn'),
            DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("cscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        RefitterParameters = cms.PSet(
            FitterName = cms.string('KFFitterSmootherSTA'),
            MaxFractionOfLostHits = cms.double(0.05),
            ForceAllIterations = cms.bool(False),
            NumberOfIterations = cms.uint32(3),
            RescaleError = cms.double(100.0)
        )
    )
)


process.standAloneSETMuons = cms.EDProducer("StandAloneMuonProducer",
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(True)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    InputObjects = cms.InputTag("SETMuonSeed"),
    MuonTrajectoryBuilder = cms.string('DirectMuonTrajectoryBuilder'),
    STATrajBuilderParameters = cms.PSet(
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('KFFitterSmootherSTA'),
            MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            UseSubRecHits = cms.bool(False),
            NMinRecHits = cms.uint32(2),
            RescaleError = cms.double(1.0)
        )
    )
)


process.stripPairElectronSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('stripPairElectronSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.4),
            ptMin = cms.double(1.0),
            originHalfLength = cms.double(12.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.tevMuons = cms.EDProducer("TevMuonProducer",
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    RefitIndex = cms.vint32(1, 2, 3, 4),
    RefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32(-1),
        MuonHitsOption = cms.int32(1),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        RefitDirection = cms.string('insideOut'),
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        Propagator = cms.string('SmartPropagatorAnyRK'),
        TrackerSkipSystem = cms.int32(-1),
        DoPredictionsOnly = cms.bool(False),
        Chi2ProbabilityCut = cms.double(30.0),
        PropDirForCosmics = cms.bool(False),
        HitThreshold = cms.int32(1),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        Chi2CutCSC = cms.double(1.0),
        Chi2CutRPC = cms.double(1.0),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        DYTthrs = cms.vint32(10, 5),
        RefitRPCHits = cms.bool(True),
        Chi2CutDT = cms.double(30.0),
        PtCut = cms.double(1.0),
        SkipStation = cms.int32(-1)
    ),
    Refits = cms.vstring('default', 
        'firstHit', 
        'picky', 
        'dyt'),
    MuonCollectionLabel = cms.InputTag("globalMuons")
)


process.tobTecStepClusters = cms.EDProducer("TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    trajectories = cms.InputTag("pixelLessStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("pixelLessStepSelector","pixelLessStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.tobTecStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('tobTecStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(6.0),
            ptMin = cms.double(0.6),
            originHalfLength = cms.double(30.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.tobTecStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("tobTecStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(2),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(5),
        chi2n_par = cms.double(0.4),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.8, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.8, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('tobTecStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(2.0, 4.0),
        d0_par1 = cms.vdouble(2.0, 4.0),
        preFilterName = cms.string(''),
        minHitsToBypassChecks = cms.uint32(20)
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(2),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.3),
            dz_par1 = cms.vdouble(1.4, 4.0),
            dz_par2 = cms.vdouble(1.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('tobTecStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('tobTecStepLoose'),
            d0_par2 = cms.vdouble(1.5, 4.0),
            d0_par1 = cms.vdouble(1.5, 4.0),
            res_par = cms.vdouble(0.003, 0.001),
            minHitsToBypassChecks = cms.uint32(20)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(2),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.2),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.3, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.3, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('tobTecStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.4, 4.0),
            d0_par1 = cms.vdouble(1.4, 4.0),
            preFilterName = cms.string('tobTecStepTight'),
            minHitsToBypassChecks = cms.uint32(20)
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.tobTecStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("tobTecStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    TrajectoryBuilder = cms.string('tobTecStepTrajectoryBuilder'),
    numHitsForSeedCleaner = cms.int32(50)
)


process.tobTecStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("tobTecStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('tobTecFlexibleKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter6'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.topBottomClusterInfoProducer = cms.EDProducer("TopBottomClusterInfoProducer",
    pixelClustersNew = cms.InputTag("siPixelClustersTop"),
    stripStereoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    stripMonoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    stripClustersOld = cms.InputTag("siStripClusters"),
    pixelHitsNew = cms.InputTag("siPixelRecHitsTop"),
    pixelHitsOld = cms.InputTag("siPixelRecHits"),
    pixelClustersOld = cms.InputTag("siPixelClusters"),
    stripClustersNew = cms.InputTag("siStripClustersTop"),
    stripMonoHitsOld = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stripStereoHitsOld = cms.InputTag("siStripMatchedRecHits","stereoRecHit")
)


process.topBottomClusterInfoProducerBottom = cms.EDProducer("TopBottomClusterInfoProducer",
    stripStereoHitsNew = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit"),
    stripMonoHitsNew = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    stripClustersOld = cms.InputTag("siStripClusters"),
    pixelHitsNew = cms.InputTag("siPixelRecHitsBottom"),
    pixelHitsOld = cms.InputTag("siPixelRecHits"),
    stripStereoHitsOld = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    pixelClustersOld = cms.InputTag("siPixelClusters"),
    stripClustersNew = cms.InputTag("siStripClustersBottom"),
    stripMonoHitsOld = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    pixelClustersNew = cms.InputTag("siPixelClustersBottom")
)


process.topBottomClusterInfoProducerTop = cms.EDProducer("TopBottomClusterInfoProducer",
    stripStereoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    stripMonoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    stripClustersOld = cms.InputTag("siStripClusters"),
    pixelHitsNew = cms.InputTag("siPixelRecHitsTop"),
    pixelHitsOld = cms.InputTag("siPixelRecHits"),
    stripStereoHitsOld = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    pixelClustersOld = cms.InputTag("siPixelClusters"),
    stripClustersNew = cms.InputTag("siStripClustersTop"),
    stripMonoHitsOld = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    pixelClustersNew = cms.InputTag("siPixelClustersTop")
)


process.trackExtrapolator = cms.EDProducer("TrackExtrapolator",
    trackQuality = cms.string('goodIterative'),
    trackSrc = cms.InputTag("generalTracks")
)


process.tripletElectronClusterMask = cms.EDProducer("SeedClusterRemover",
    trajectories = cms.InputTag("tripletElectronSeeds"),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.tripletElectronSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('tripletElectronSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(0.02),
            nSigmaZ = cms.double(4.0),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            ptMin = cms.double(1.0)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.HSCParticleProducer = cms.EDFilter("HSCParticleProducer",
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    EERecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    EBRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    maxInvPtDiff = cms.double(0.005),
    useBetaFromTk = cms.bool(True),
    minSAMuPt = cms.double(70),
    minTkHits = cms.uint32(3),
    useBetaFromEcal = cms.bool(False),
    SelectionParameters = cms.VPSet(cms.PSet(
        maxMuTimeDtBeta = cms.double(-1),
        onlyConsiderMuonTK = cms.bool(False),
        maxBetaRpc = cms.double(-1),
        onlyConsiderMuonSTA = cms.bool(False),
        onlyConsiderRpc = cms.bool(False),
        minMuTimeDtNdof = cms.double(-1),
        minTrackHits = cms.int32(3),
        minMuTimeCombinedNdof = cms.double(-1),
        onlyConsiderTrack = cms.bool(False),
        minMuonP = cms.double(-1),
        minMTMuonPt = cms.double(-1),
        onlyConsiderMuonGB = cms.bool(False),
        minMuonPt = cms.double(5.0),
        minMuTimeCscNdof = cms.double(-1),
        maxMuTimeCscBeta = cms.double(-1),
        maxBetaEcal = cms.double(-1),
        onlyConsiderMTMuon = cms.bool(False),
        minDedx = cms.double(-1),
        minTrackPt = cms.double(45.0),
        onlyConsiderEcal = cms.bool(False),
        maxMuTimeCombinedBeta = cms.double(-1),
        minSAMuonPt = cms.double(-1),
        minTrackP = cms.double(-1),
        onlyConsiderMuon = cms.bool(False)
    ), 
        cms.PSet(
            maxMuTimeDtBeta = cms.double(-1),
            onlyConsiderMuonTK = cms.bool(False),
            maxBetaRpc = cms.double(-1),
            onlyConsiderMuonSTA = cms.bool(False),
            onlyConsiderRpc = cms.bool(False),
            minMuTimeDtNdof = cms.double(-1),
            minTrackHits = cms.int32(-1),
            minMuTimeCombinedNdof = cms.double(-1),
            onlyConsiderTrack = cms.bool(False),
            minMuonP = cms.double(-1),
            minMTMuonPt = cms.double(70.0),
            onlyConsiderMuonGB = cms.bool(False),
            minMuonPt = cms.double(-1),
            minMuTimeCscNdof = cms.double(-1),
            maxMuTimeCscBeta = cms.double(-1),
            maxBetaEcal = cms.double(-1),
            onlyConsiderMTMuon = cms.bool(True),
            minDedx = cms.double(-1),
            minTrackPt = cms.double(-1),
            onlyConsiderEcal = cms.bool(False),
            maxMuTimeCombinedBeta = cms.double(-1),
            minSAMuonPt = cms.double(-1),
            minTrackP = cms.double(-1),
            onlyConsiderMuon = cms.bool(False)
        ), 
        cms.PSet(
            maxMuTimeDtBeta = cms.double(-1),
            onlyConsiderMuonTK = cms.bool(False),
            maxBetaRpc = cms.double(-1),
            onlyConsiderMuonSTA = cms.bool(True),
            onlyConsiderRpc = cms.bool(False),
            minMuTimeDtNdof = cms.double(-1),
            minTrackHits = cms.int32(-1),
            minMuTimeCombinedNdof = cms.double(-1),
            onlyConsiderTrack = cms.bool(False),
            minMuonP = cms.double(-1),
            minMTMuonPt = cms.double(-1),
            onlyConsiderMuonGB = cms.bool(False),
            minMuonPt = cms.double(-1),
            minMuTimeCscNdof = cms.double(-1),
            maxMuTimeCscBeta = cms.double(-1),
            maxBetaEcal = cms.double(-1),
            onlyConsiderMTMuon = cms.bool(False),
            minDedx = cms.double(-1),
            minTrackPt = cms.double(-1),
            onlyConsiderEcal = cms.bool(False),
            maxMuTimeCombinedBeta = cms.double(-1),
            minSAMuonPt = cms.double(70.0),
            minTrackP = cms.double(-1),
            onlyConsiderMuon = cms.bool(False)
        )),
    maxTkChi2 = cms.double(25),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    minDR = cms.double(0.1),
    minMTDR = cms.double(0.3),
    muons = cms.InputTag("muons"),
    tracksIsolation = cms.InputTag("generalTracks"),
    MTmuons = cms.InputTag("MTMuons"),
    useBetaFromRpc = cms.bool(True),
    tracks = cms.InputTag("TrackRefitter"),
    minMuP = cms.double(25),
    minMTMuPt = cms.double(70),
    minTkP = cms.double(25),
    filter = cms.bool(False),
    useBetaFromMuon = cms.bool(True)
)


process.HSCParticleSelector = cms.EDFilter("HSCParticleSelector",
    filter = cms.bool(True),
    SelectionParameters = cms.VPSet(cms.PSet(
        maxMuTimeDtBeta = cms.double(-1),
        onlyConsiderMuonTK = cms.bool(False),
        maxBetaRpc = cms.double(-1),
        onlyConsiderMuonSTA = cms.bool(False),
        onlyConsiderRpc = cms.bool(False),
        minMuTimeDtNdof = cms.double(-1),
        minTrackHits = cms.int32(3),
        minMuTimeCombinedNdof = cms.double(-1),
        onlyConsiderTrack = cms.bool(True),
        minMuonP = cms.double(-1),
        minMTMuonPt = cms.double(-1),
        onlyConsiderMuonGB = cms.bool(False),
        minMuonPt = cms.double(5.0),
        minMuTimeCscNdof = cms.double(-1),
        maxMuTimeCscBeta = cms.double(-1),
        maxBetaEcal = cms.double(-1),
        onlyConsiderMTMuon = cms.bool(False),
        minDedx = cms.double(-1),
        minTrackPt = cms.double(45.0),
        onlyConsiderEcal = cms.bool(False),
        maxMuTimeCombinedBeta = cms.double(-1),
        minSAMuonPt = cms.double(-1),
        minTrackP = cms.double(-1),
        onlyConsiderMuon = cms.bool(False),
        minDedxEstimator1 = cms.double(3.5)
    ), 
        cms.PSet(
            maxMuTimeDtBeta = cms.double(0.9),
            onlyConsiderMuonTK = cms.bool(False),
            maxBetaRpc = cms.double(-1),
            onlyConsiderMuonSTA = cms.bool(False),
            onlyConsiderRpc = cms.bool(False),
            minMuTimeDtNdof = cms.double(-1),
            minTrackHits = cms.int32(3),
            minMuTimeCombinedNdof = cms.double(-1),
            onlyConsiderTrack = cms.bool(False),
            minMuonP = cms.double(-1),
            minMTMuonPt = cms.double(-1),
            onlyConsiderMuonGB = cms.bool(False),
            minMuonPt = cms.double(5.0),
            minMuTimeCscNdof = cms.double(-1),
            maxMuTimeCscBeta = cms.double(-1),
            maxBetaEcal = cms.double(-1),
            onlyConsiderMTMuon = cms.bool(False),
            minDedx = cms.double(-1),
            minTrackPt = cms.double(45.0),
            onlyConsiderEcal = cms.bool(False),
            maxMuTimeCombinedBeta = cms.double(-1),
            minSAMuonPt = cms.double(-1),
            minTrackP = cms.double(-1),
            onlyConsiderMuon = cms.bool(True)
        )),
    source = cms.InputTag("HSCParticleProducer")
)


process.genParticlesReduced = cms.EDFilter("GenParticleSelector",
    filter = cms.bool(False),
    src = cms.InputTag("genParticles"),
    cut = cms.string('p > 0.2 && p < 10 && status !=2 && charge!=0')
)


process.generalTracksReduced = cms.EDFilter("TrackSelector",
    filter = cms.bool(False),
    src = cms.InputTag("ALCARECOSiStripCalMinBias"),
    cut = cms.string('p > 0.5 && p < 2.5 && trackerExpectedHitsInner.numberOfLostHits==0 && hitPattern.trackerLayersWithoutMeasurement==0')
)


process.demo = cms.EDAnalyzer("TheNtupleMaker",
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("generalTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    sdoublePF = cms.untracked.vstring('sdouble                         kt6PFJets_rho                   1', 
        'double value()'),
    Jet = cms.untracked.vstring('patJetHelper                    selectedPatJetsPFlow            200', 
        'float  energy()', 
        'float  et()', 
        'float  pt()', 
        'float  pz()', 
        'float  phi()', 
        'float  eta()', 
        'float  chargedHadronEnergyFraction()', 
        'float  neutralHadronEnergyFraction()', 
        'float  chargedEmEnergyFraction()', 
        'float  neutralEmEnergyFraction()', 
        'float  jecUnc()'),
    ElectronPFlow = cms.untracked.vstring('patElectronHelper                patElectronsLoosePFlow         200', 
        'float  energy()', 
        'float  et()', 
        'float  pz()', 
        'float  pt()', 
        'float  phi()', 
        'float  eta()', 
        'int    charge()', 
        'float  electronID("mvaNonTrigV0")', 
        'float   electronID("mvaTrigV0")', 
        'bool    passConversionVeto()', 
        'int     gsfTrack()->trackerExpectedHitsInner().numberOfLostHits()', 
        'float   superCluster()->eta()', 
        'float   chargedHadronIso()', 
        'float   neutralHadronIso()', 
        'float   photonIso()', 
        'float   puChargedHadronIso()', 
        'float   Aeff04()'),
    MuonPFlow = cms.untracked.vstring('patMuon                         selectedPatMuonsLoosePFlow      200', 
        'float  energy()', 
        'float  et()', 
        'float  pz()', 
        'float  pt()', 
        'float  phi()', 
        'float  eta()', 
        'int    charge()', 
        'bool    isPFMuon()', 
        'bool    isGlobalMuon()', 
        'bool    isTrackerMuon()', 
        'bool    isStandAloneMuon()', 
        'float   globalTrack().chi2()', 
        'float   globalTrack().ndof()', 
        'float   globalTrack().d0()', 
        'float   dB()', 
        'float   vertex().z()', 
        'float   innerTrack()->dz()', 
        'int     globalTrack()->hitPattern().numberOfValidMuonHits()', 
        'int     innerTrack()->hitPattern().trackerLayersWithMeasurement()', 
        'int     innerTrack()->hitPattern().numberOfValidPixelHits()', 
        'int     numberOfMatchedStations()', 
        'float   chargedHadronIso()', 
        'float   neutralHadronIso()', 
        'float   photonIso()', 
        'float   puChargedHadronIso()'),
    SimTrack = cms.untracked.vstring('SimTrack                        g4SimHits                      5000', 
        'float  charge()', 
        'int  vertIndex()', 
        'bool  noVertex()', 
        'int  genpartIndex()', 
        'bool  noGenpart()', 
        'int  type()', 
        'unsigned int  trackId()', 
        'float momentum().pt()', 
        'float momentum().phi()', 
        'float momentum().eta()', 
        'float momentum().energy()'),
    buffers = cms.untracked.vstring('edmEventHelper', 
        'PileupSummaryInfo', 
        'Track', 
        'GenParticle'),
    edmEventHelper = cms.untracked.vstring('edmEventHelper                  info                              1', 
        '   bool  isRealData()', 
        '   int   run()', 
        '   int   event()', 
        '   int   luminosityBlock()', 
        '   int   bunchCrossing()', 
        '   int   orbitNumber()'),
    GenParticle = cms.untracked.vstring('recoGenParticle                 genParticlesReduced             2000', 
        'int    charge()', 
        'float  energy()', 
        'float  et()', 
        'float  pz()', 
        'float  pt()', 
        'float  phi()', 
        'float  eta()', 
        'int    pdgId()', 
        'int    status()'),
    Track = cms.untracked.vstring('recoTrackHelper                       TrackRefitter            2000', 
        'float  pt()', 
        'float  ptError()', 
        'float  px()', 
        'float  py()', 
        'float  pz()', 
        'float  phi()', 
        'float  eta()', 
        'float  vx()', 
        'float  vy()', 
        'float  vz()', 
        'float  chi2()', 
        'float  ndof()', 
        'float  charge()', 
        'unsigned short  numberOfValidHits()', 
        'unsigned short  hitPattern().trackerLayersWithoutMeasurement()', 
        'unsigned short  trackerExpectedHitsInner().numberOfLostHits()', 
        'unsigned short  trackerExpectedHitsOuter().numberOfHits()', 
        'bool    trackHighPurity()', 
        'float  dEdxNPASmi()', 
        'float  dEdxASmi()', 
        'unsigned int     dEdxNPNoM()', 
        'unsigned int     dEdxNoM()'),
    Vertex = cms.untracked.vstring('recoVertex                      offlinePrimaryVertices          100', 
        'float  ndof()', 
        'float  x()', 
        'float  y()', 
        'float  z()', 
        'float position().rho()'),
    GenJet = cms.untracked.vstring('recoGenJet                    ak5GenJets                         200', 
        'float  energy()', 
        'float  et()', 
        'float  pt()', 
        'float  pz()', 
        'float  phi()', 
        'float  eta()'),
    Electron = cms.untracked.vstring('patElectronHelper                 selectedPatElectrons          200', 
        'float  energy()', 
        'float  et()', 
        'float  pz()', 
        'float  pt()', 
        'float  phi()', 
        'float  eta()', 
        'int    charge()', 
        'float  electronID("mvaNonTrigV0")', 
        'float   electronID("mvaTrigV0")', 
        'bool    passConversionVeto()', 
        'int     gsfTrack()->trackerExpectedHitsInner().numberOfLostHits()', 
        'float   superCluster()->eta()', 
        'float   chargedHadronIso()', 
        'float   neutralHadronIso()', 
        'float   photonIso()', 
        'float   puChargedHadronIso()', 
        'float   Aeff04()'),
    PileupSummaryInfo = cms.untracked.vstring('PileupSummaryInfo               addPileupInfo                    10', 
        ' int getBunchCrossing()', 
        ' int getPU_NumInteractions()', 
        ' float getTrueNumInteractions()'),
    isRECOfile = cms.untracked.bool(True),
    isALCARECOfile = cms.untracked.bool(True),
    edmEventHelperExtra = cms.untracked.vstring('edmEventHelperExtra             Event::edm                        1'),
    Tau = cms.untracked.vstring('patTau                          selectedPatTaus                 200', 
        'float  energy()', 
        'float  et()', 
        'float  pz()', 
        'float  pt()', 
        'float  phi()', 
        'float  eta()', 
        'int    charge()', 
        'float  tauID("byLooseCombinedIsolationDeltaBetaCorr")', 
        'float  tauID("decayModeFinding")', 
        'float  tauID("againstElectronLoose")', 
        'float  tauID("againstMuonTight")'),
    edmTriggerResultsHelper = cms.untracked.vstring('edmTriggerResultsHelper TriggerResults::HLT 1', 
        ' int value("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v1...20") value_HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v', 
        ' int value("HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v1...20") value_HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v', 
        ' int value("HLT_MET120_HBHENoiseCleaned_v1...20") value_HLT_MET120_HBHENoiseCleaned_v', 
        ' int prescale("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v1...20") prescale_HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v', 
        ' int prescale("HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v1...20") prescale_HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v', 
        ' int prescale("HLT_MET120_HBHENoiseCleaned_v1...20") prescale_HLT_MET120_HBHENoiseCleaned_v'),
    SimVertex = cms.untracked.vstring('SimVertex                       g4SimHits                      5000', 
        'int  parentIndex()', 
        'bool  noParent()', 
        'unsigned int  vertexId()', 
        'float position().x()', 
        'float position().y()', 
        'float position().z()', 
        'float position().t()'),
    sdouble = cms.untracked.vstring('sdouble                         kt6CaloJets_rho                   1', 
        'float value()'),
    Muon = cms.untracked.vstring('patMuon                         selectedPatMuonsLoose           200', 
        'float  energy()', 
        'float  et()', 
        'float  pz()', 
        'float  pt()', 
        'float  phi()', 
        'float  eta()', 
        'int    charge()', 
        'bool    isPFMuon()', 
        'bool    isGlobalMuon()', 
        'bool    isTrackerMuon()', 
        'bool    isStandAloneMuon()', 
        'float   globalTrack().chi2()', 
        'float   globalTrack().ndof()', 
        'float   globalTrack().d0()', 
        'float   dB()', 
        'float   vertex().z()', 
        'float   innerTrack()->dz()', 
        'int     globalTrack()->hitPattern().numberOfValidMuonHits()', 
        'int     innerTrack()->hitPattern().trackerLayersWithMeasurement()', 
        'int     innerTrack()->hitPattern().numberOfValidPixelHits()', 
        'int     numberOfMatchedStations()', 
        'float   chargedHadronIso()', 
        'float   neutralHadronIso()', 
        'float   photonIso()', 
        'float   puChargedHadronIso()'),
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    MET = cms.untracked.vstring('patMET                          patMETsPFlow                      1', 
        'float  energy()', 
        'float  et()', 
        'float  pz()', 
        'float  pt()', 
        'float  phi()', 
        'float  eta()'),
    ntupleName = cms.untracked.string('ntuple.root'),
    analyzerName = cms.untracked.string('analyzer.cc')
)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('out_alcareco_data.root'),
    dropMetaData = cms.untracked.string('ALL'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *')
)


process.cosmicsMuonIdSequence = cms.Sequence(process.cosmicsVetoSeeds+process.cosmicsVetoTrackCandidates+process.cosmicsVetoTracksRaw+process.cosmicsVetoTracks+process.cosmicsVeto)


process.doAlldEdXEstimatorsCTF = cms.Sequence(process.dedxTruncated40CTF+process.dedxDiscrimASmiCTF+process.dedxHarmonic2CTF)


process.rstracksP5Top = cms.Sequence(process.roadSearchSeedsP5Top+process.roadSearchCloudsP5Top+process.rsTrackCandidatesP5Top+process.rsWithMaterialTracksP5Top)


process.regionalCosmicTracksSeq = cms.Sequence(process.regionalCosmicTrackerSeeds+process.regionalCosmicCkfTrackCandidates+process.regionalCosmicTracks)


process.rstracksP5 = cms.Sequence(process.roadSearchSeedsP5+process.roadSearchCloudsP5+process.rsTrackCandidatesP5+process.rsWithMaterialTracksCosmics+process.rsWithMaterialTracksP5)


process.doAlldEdXDiscriminators = cms.Sequence(process.dedxDiscrimProd+process.dedxDiscrimBTag+process.dedxDiscrimSmi+process.dedxDiscrimASmi)


process.rstracksP5Bottom = cms.Sequence(process.roadSearchSeedsP5Bottom+process.roadSearchCloudsP5Bottom+process.rsTrackCandidatesP5Bottom+process.rsWithMaterialTracksP5Bottom)


process.PixelLessStep = cms.Sequence(process.pixelLessStepClusters+process.pixelLessStepSeeds+process.pixelLessStepTrackCandidates+process.pixelLessStepTracks+process.pixelLessStepSelector)


process.muonSelectionTypeSequence = cms.Sequence(process.muidTrackerMuonArbitrated+process.muidAllArbitrated+process.muidGlobalMuonPromptTight+process.muidTMLastStationLoose+process.muidTMLastStationTight+process.muidTM2DCompatibilityLoose+process.muidTM2DCompatibilityTight+process.muidTMOneStationLoose+process.muidTMOneStationTight+process.muidTMLastStationOptimizedLowPtLoose+process.muidTMLastStationOptimizedLowPtTight+process.muidGMTkChiCompatibility+process.muidGMStaChiCompatibility+process.muidGMTkKinkTight+process.muidTMLastStationAngLoose+process.muidTMLastStationAngTight+process.muidTMOneStationAngLoose+process.muidTMOneStationAngTight)


process.doAlldEdXEstimatorsCTFP5LHC = cms.Sequence(process.dedxTruncated40CTFP5LHC+process.dedxDiscrimASmiCTFP5LHC+process.dedxHarmonic2CTFP5LHC)


process.ctftracksP5 = cms.Sequence(process.combinatorialcosmicseedfinderP5+process.simpleCosmicBONSeeds+process.combinedP5SeedsForCTF+process.ckfTrackCandidatesP5+process.ctfWithMaterialTracksCosmics+process.ctfWithMaterialTracksP5+process.ckfTrackCandidatesP5LHCNavigation+process.ctfWithMaterialTracksP5LHCNavigation)


process.doAlldEdXEstimatorsRS = cms.Sequence(process.dedxTruncated40RS+process.dedxDiscrimASmiRS+process.dedxHarmonic2RS)


process.muIsoDeposits_ParamGlobalMuons = cms.Sequence(process.muParamGlobalIsoDepositTk+process.muParamGlobalIsoDepositCalByAssociatorTowers+process.muParamGlobalIsoDepositJets)


process.cosmictracksP5Top = cms.Sequence(process.cosmicseedfinderP5Top+process.cosmicCandidateFinderP5Top+process.cosmictrackfinderP5Top)


process.trackerlocalrecoTop = cms.Sequence(process.siPixelClustersTop+process.siPixelRecHitsTop+process.siStripClustersTop+process.siStripMatchedRecHitsTop+process.topBottomClusterInfoProducerTop)


process.ctftracksP5Top = cms.Sequence(process.combinatorialcosmicseedfinderP5Top+process.simpleCosmicBONSeedsTop+process.combinedP5SeedsForCTFTop+process.ckfTrackCandidatesP5Top+process.ctfWithMaterialTracksP5Top)


process.muIsoDeposits_ParamGlobalMuonsOld = cms.Sequence(process.muParamGlobalIsoDepositGsTk+process.muParamGlobalIsoDepositCalEcal+process.muParamGlobalIsoDepositCalHcal)


process.muoncosmicreco1legSTA = cms.Sequence(process.CosmicMuonSeed+process.cosmicMuons1Leg)


process.striptrackerlocalreco = cms.Sequence(process.siStripZeroSuppression+process.siStripClusters+process.siStripMatchedRecHits)


process.DetachedTripletStep = cms.Sequence(process.detachedTripletStepClusters+process.detachedTripletStepSeeds+process.detachedTripletStepTrackCandidates+process.detachedTripletStepTracks+process.detachedTripletStepSelector+process.detachedTripletStep)


process.beamhaloTracksSeq = cms.Sequence(process.beamhaloTrackerSeeds+process.beamhaloTrackCandidates+process.beamhaloTracks)


process.PixelPairStep = cms.Sequence(process.pixelPairStepClusters+process.pixelPairStepSeeds+process.pixelPairStepTrackCandidates+process.pixelPairStepTracks+process.pixelPairStepSelector)


process.standAloneMuonSeeds = cms.Sequence(process.ancientMuonSeed)


process.muoncosmicreco2legsHighLevel = cms.Sequence(process.globalCosmicMuons+process.muonsFromCosmics)


process.HSCParticleProducerSeq = cms.Sequence(process.offlineBeamSpot+process.TrackRefitter+process.dedxHarm2+process.dedxTru40+process.dedxNPHarm2+process.dedxNPTru40+process.dedxNSHarm2+process.dedxNSTru40+process.dedxProd+process.dedxASmi+process.dedxNPProd+process.dedxNPASmi+process.dedxNSTHarm2+process.dedxHitInfo)


process.electronSeedsSeq = cms.Sequence(process.initialStepSeedClusterMask+process.pixelPairStepSeedClusterMask+process.mixedTripletStepSeedClusterMask+process.pixelLessStepSeedClusterMask+process.tripletElectronSeeds+process.tripletElectronClusterMask+process.pixelPairElectronSeeds+process.stripPairElectronSeeds+process.newCombinedSeeds)


process.ctfTracksCombinedSeeds = cms.Sequence(process.globalSeedsFromPairsWithVertices+process.globalSeedsFromTriplets+process.globalCombinedSeeds+process.ckfTrackCandidatesCombinedSeeds+process.ctfCombinedSeeds)


process.muIsolation_ParamGlobalMuonsOld = cms.Sequence(process.muIsoDeposits_ParamGlobalMuonsOld)


process.muoncosmicreco2legsSTA = cms.Sequence(process.CosmicMuonSeed+process.cosmicMuons)


process.muoncosmicreco1legHighLevel = cms.Sequence(process.globalCosmicMuons1Leg+process.muonsFromCosmics1Leg)


process.TobTecStep = cms.Sequence(process.tobTecStepClusters+process.tobTecStepSeeds+process.tobTecStepTrackCandidates+process.tobTecStepTracks+process.tobTecStepSelector)


process.ctfTracksPixelLess = cms.Sequence(process.globalPixelLessSeeds+process.ckfTrackCandidatesPixelLess+process.ctfPixelLess)


process.muonIdProducerSequence = cms.Sequence(process.glbTrackQual+process.muons1stStep+process.calomuons+process.muonEcalDetIds+process.muonShowerInformation)


process.ConvStep = cms.Sequence(process.convClusters+process.photonConvTrajSeedFromSingleLeg+process.convTrackCandidates+process.convStepTracks+process.convStepSelector)


process.doAlldEdXEstimatorsCosmicTF = cms.Sequence(process.dedxTruncated40CosmicTF+process.dedxDiscrimASmiCosmicTF+process.dedxHarmonic2CosmicTF)


process.LowPtTripletStep = cms.Sequence(process.lowPtTripletStepClusters+process.lowPtTripletStepSeeds+process.lowPtTripletStepTrackCandidates+process.lowPtTripletStepTracks+process.lowPtTripletStepSelector)


process.ctfTracksNoOverlaps = cms.Sequence(process.ckfTrackCandidatesNoOverlaps+process.ctfNoOverlaps)


process.rstracks = cms.Sequence(process.roadSearchSeeds+process.roadSearchClouds+process.rsTrackCandidates+process.rsWithMaterialTracks)


process.muontracking = cms.Sequence(process.standAloneMuonSeeds+process.standAloneMuons+process.globalMuons+process.refittedStandAloneMuons)


process.trackerlocalrecoBottom = cms.Sequence(process.siPixelClustersBottom+process.siPixelRecHitsBottom+process.siStripClustersBottom+process.siStripMatchedRecHitsBottom+process.topBottomClusterInfoProducerBottom)


process.muIsoDeposits_muons = cms.Sequence(process.muIsoDepositTk+process.muIsoDepositCalByAssociatorTowers+process.muIsoDepositJets)


process.MuonOnlySeq = cms.Sequence(process.ancientMuonSeed+process.MTancientMuonSeed+process.MTSAMuons+process.RefitMTSAMuons+process.MTMuons+process.MuonSegmentProducer+process.MTmuontiming+process.refittedStandAloneMuons)


process.MixedTripletStep = cms.Sequence(process.mixedTripletStepClusters+process.mixedTripletStepSeedsA+process.mixedTripletStepSeedsB+process.mixedTripletStepSeeds+process.mixedTripletStepTrackCandidates+process.mixedTripletStepTracks+process.mixedTripletStepSelector+process.mixedTripletStep)


process.tracksP5Top = cms.Sequence(process.ctftracksP5Top+process.cosmictracksP5Top)


process.pixeltrackerlocalreco = cms.Sequence(process.siPixelClusters+process.siPixelRecHits)


process.muontracking_with_SET = cms.Sequence(process.SETMuonSeed+process.standAloneSETMuons+process.globalSETMuons)


process.ctftracksP5Bottom = cms.Sequence(process.combinatorialcosmicseedfinderP5Bottom+process.simpleCosmicBONSeedsBottom+process.combinedP5SeedsForCTFBottom+process.ckfTrackCandidatesP5Bottom+process.ctfWithMaterialTracksP5Bottom)


process.cosmictracksP5 = cms.Sequence(process.cosmicseedfinderP5+process.cosmicCandidateFinderP5+process.cosmictrackfinderCosmics+process.cosmictrackfinderP5+process.cosmicTrackSplitter+process.splittedTracksP5)


process.cosmictracksP5Bottom = cms.Sequence(process.cosmicseedfinderP5Bottom+process.cosmicCandidateFinderP5Bottom+process.cosmictrackfinderP5Bottom)


process.doAlldEdXEstimators = cms.Sequence(process.dedxTruncated40+process.dedxHarmonic2+process.dedxDiscrimASmi)


process.muonPFIsolationDepositsSequence = cms.Sequence(process.muPFIsoDepositCharged+process.muPFIsoDepositChargedAll+process.muPFIsoDepositGamma+process.muPFIsoDepositNeutral+process.muPFIsoDepositPU)


process.InitialStep = cms.Sequence(process.initialStepSeeds+process.initialStepTrackCandidates+process.initialStepTracks+process.initialStepSelector)


process.muonreco_with_SET = cms.Sequence(process.muontracking_with_SET)


process.trackerlocalreco = cms.Sequence(process.pixeltrackerlocalreco+process.striptrackerlocalreco)


process.muIsolation_ParamGlobalMuons = cms.Sequence(process.muIsoDeposits_ParamGlobalMuons)


process.muonreco = cms.Sequence(process.muontracking+process.muonIdProducerSequence)


process.tracksP5Bottom = cms.Sequence(process.ctftracksP5Bottom+process.cosmictracksP5Bottom)


process.muontracking_with_TeVRefinement = cms.Sequence(process.muontracking+process.tevMuons)


process.muonPFIsolationSequence = cms.Sequence(process.muonPFIsolationDepositsSequence+process.muPFIsoValueCharged03+process.muPFIsoValueChargedAll03+process.muPFIsoValueGamma03+process.muPFIsoValueNeutral03+process.muPFIsoValueGammaHighThreshold03+process.muPFIsoValueNeutralHighThreshold03+process.muPFIsoValuePU03+process.muPFIsoValueCharged04+process.muPFIsoValueChargedAll04+process.muPFIsoValueGamma04+process.muPFIsoValueNeutral04+process.muPFIsoValueGammaHighThreshold04+process.muPFIsoValueNeutralHighThreshold04+process.muPFIsoValuePU04)


process.muoncosmicreco = cms.Sequence(process.muoncosmicreco2legsSTA+process.muoncosmicreco1legSTA)


process.muoncosmichighlevelreco = cms.Sequence(process.muoncosmicreco2legsHighLevel+process.muoncosmicreco1legHighLevel+process.cosmicsMuonIdSequence)


process.trackerCosmics_TopBot = cms.Sequence(process.trackerlocalrecoTop+process.tracksP5Top+process.trackerlocalrecoBottom+process.tracksP5Bottom)


process.iterTracking = cms.Sequence(process.InitialStep+process.LowPtTripletStep+process.PixelPairStep+process.DetachedTripletStep+process.MixedTripletStep+process.PixelLessStep+process.TobTecStep+process.generalTracks+process.ConvStep+process.conversionStepTracks)


process.muonshighlevelreco = cms.Sequence(process.muonPFIsolationSequence+process.muons)


process.ckftracks_woBH = cms.Sequence(process.iterTracking+process.electronSeedsSeq+process.doAlldEdXEstimators)


process.muIsolation_muons = cms.Sequence(process.muIsoDeposits_muons)


process.doAllCosmicdEdXEstimators = cms.Sequence(process.doAlldEdXEstimatorsCTF+process.doAlldEdXEstimatorsCosmicTF+process.doAlldEdXEstimatorsCTFP5LHC)


process.muonrecowith_TeVRefinemen = cms.Sequence(process.muontracking_with_TeVRefinement+process.muonIdProducerSequence)


process.ckftracks_wodEdX = cms.Sequence(process.iterTracking+process.electronSeedsSeq)


process.ckftracks = cms.Sequence(process.iterTracking+process.electronSeedsSeq+process.doAlldEdXEstimators)


process.ckftracks_plus_pixelless = cms.Sequence(process.ckftracks+process.ctfTracksPixelLess)


process.trackingGlobalReco = cms.Sequence(process.ckftracks+process.trackExtrapolator)


process.tracksP5_wodEdX = cms.Sequence(process.cosmictracksP5+process.ctftracksP5+process.trackerCosmics_TopBot)


process.tracksP5 = cms.Sequence(process.cosmictracksP5+process.ctftracksP5+process.trackerCosmics_TopBot+process.doAllCosmicdEdXEstimators)


process.muIsolation = cms.Sequence(process.muIsolation_muons)


process.muonreco_plus_isolation = cms.Sequence(process.muonrecowith_TeVRefinemen+process.muIsolation)


process.muonrecoComplete_minus_SET_minus_muIDmaps = cms.Sequence(process.muonrecowith_TeVRefinemen+process.muIsolation)


process.muonreco_plus_isolation_plus_SET = cms.Sequence(process.muonrecowith_TeVRefinemen+process.muonreco_with_SET+process.muIsolation)


process.muonrecoComplete = cms.Sequence(process.muonreco_plus_isolation_plus_SET+process.muonSelectionTypeSequence)


process.muonrecoComplete_minus_muIDmaps = cms.Sequence(process.muonreco_plus_isolation_plus_SET)


process.muonreco_plus_isolation_plus_SET_plus_muIDmaps = cms.Sequence(process.muonreco_plus_isolation_plus_SET+process.muonSelectionTypeSequence)


process.pPF = cms.Path(process.generalTracksReduced+process.HSCParticleProducerSeq+process.demo)


process.outpath = cms.EndPath(process.out)


process.DQMStore = cms.Service("DQMStore")


process.MessageLogger = cms.Service("MessageLogger",
    suppressInfo = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    suppressDebug = cms.untracked.vstring(),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    cerr_stats = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        output = cms.untracked.string('cerr'),
        optionalPSet = cms.untracked.bool(True)
    ),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noTimeStamps = cms.untracked.bool(False),
        FwkReport = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1000),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(5)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        threshold = cms.untracked.string('INFO'),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        FwkSummary = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    FrameworkJobReport = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring(),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    debugModules = cms.untracked.vstring(),
    infos = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport')
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    horeco = cms.PSet(
        initialSeed = cms.untracked.uint32(541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    paramMuons = cms.PSet(
        initialSeed = cms.untracked.uint32(54525),
        engineName = cms.untracked.string('TRandom3')
    ),
    saveFileName = cms.untracked.string(''),
    hbhereco = cms.PSet(
        initialSeed = cms.untracked.uint32(541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    externalLHEProducer = cms.PSet(
        initialSeed = cms.untracked.uint32(234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    famosPileUp = cms.PSet(
        initialSeed = cms.untracked.uint32(918273),
        engineName = cms.untracked.string('TRandom3')
    ),
    simMuonDTDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        initialSeed = cms.untracked.uint32(24680),
        engineName = cms.untracked.string('TRandom3')
    ),
    ecalPreshowerRecHit = cms.PSet(
        initialSeed = cms.untracked.uint32(6541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    generator = cms.PSet(
        initialSeed = cms.untracked.uint32(123456789),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simMuonRPCDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    hiSignal = cms.PSet(
        initialSeed = cms.untracked.uint32(123456789),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simCastorDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(12345678),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    mix = cms.PSet(
        initialSeed = cms.untracked.uint32(12345),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    VtxSmeared = cms.PSet(
        initialSeed = cms.untracked.uint32(98765432),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    LHCTransport = cms.PSet(
        initialSeed = cms.untracked.uint32(87654321),
        engineName = cms.untracked.string('TRandom3')
    ),
    ecalRecHit = cms.PSet(
        initialSeed = cms.untracked.uint32(654321),
        engineName = cms.untracked.string('TRandom3')
    ),
    hfreco = cms.PSet(
        initialSeed = cms.untracked.uint32(541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    simSiStripDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simEcalUnsuppressedDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    hiSignalG4SimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(11),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    famosSimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(13579),
        engineName = cms.untracked.string('TRandom3')
    ),
    MuonSimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(987346),
        engineName = cms.untracked.string('TRandom3')
    ),
    g4SimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(11),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    hiSignalLHCTransport = cms.PSet(
        initialSeed = cms.untracked.uint32(88776655),
        engineName = cms.untracked.string('TRandom3')
    ),
    mixGenPU = cms.PSet(
        initialSeed = cms.untracked.uint32(918273),
        engineName = cms.untracked.string('TRandom3')
    ),
    l1ParamMuons = cms.PSet(
        initialSeed = cms.untracked.uint32(6453209),
        engineName = cms.untracked.string('TRandom3')
    ),
    simBeamSpotFilter = cms.PSet(
        initialSeed = cms.untracked.uint32(87654321),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simHcalUnsuppressedDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(11223344),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simMuonCSCDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(11223344),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    mixData = cms.PSet(
        initialSeed = cms.untracked.uint32(12345),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simSiPixelDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    )
)


process.UpdaterService = cms.Service("UpdaterService")


process.AnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnalyticalPropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    PropagationDirection = cms.string('anyDirection')
)


process.BeamHaloMPropagatorAlong = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('BeamHaloMPropagatorAlong'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(10000),
    useRungeKutta = cms.bool(True)
)


process.BeamHaloMPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('BeamHaloMPropagatorOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(10000),
    useRungeKutta = cms.bool(True)
)


process.BeamHaloPropagatorAlong = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorAlong'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorAlong')
)


process.BeamHaloPropagatorAny = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorAny'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorAny'),
    PropagationDirection = cms.string('anyDirection'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorAlong')
)


process.BeamHaloPropagatorOpposite = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorOpposite'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorOpposite')
)


process.BeamHaloSHPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorAlong'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.BeamHaloSHPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorAny'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.BeamHaloSHPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorOpposite'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string(''),
    useDDD = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string(''),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerHardcodeGeometryEP = cms.ESProducer("CaloTowerHardcodeGeometryEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorHardcodeGeometryEP = cms.ESProducer("CastorHardcodeGeometryEP")


process.Chi2EstimatorForMuRefit = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(100000.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('Chi2EstimatorForMuRefit')
)


process.Chi2EstimatorForMuonTrackLoader = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(100000.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('Chi2EstimatorForMuonTrackLoader')
)


process.Chi2EstimatorForRefit = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(100000.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('Chi2EstimatorForRefit')
)


process.Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(30.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('Chi2')
)


process.CkfTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('CkfTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    MeasurementTrackerName = cms.string(''),
    estimator = cms.string('Chi2'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.CkfTrajectoryBuilderBeamHalo = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('BeamHaloPropagatorAlong'),
    trajectoryFilterName = cms.string('ckfTrajectoryFilterBeamHaloMuon'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('CkfTrajectoryBuilderBH'),
    propagatorOpposite = cms.string('BeamHaloPropagatorOpposite'),
    MeasurementTrackerName = cms.string(''),
    estimator = cms.string('Chi2'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter')
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.DummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('DummyDetLayerGeometry')
)


process.EcalBarrelGeometryEP = cms.ESProducer("EcalBarrelGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryEP = cms.ESProducer("EcalEndcapGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryEP = cms.ESProducer("EcalPreshowerGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.EstimatorForSTA = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(1000.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('Chi2STA')
)


process.FittingSmootherRKP5 = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('RKFitter'),
    MinNumberOfHits = cms.int32(4),
    Smoother = cms.string('RKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('FittingSmootherRKP5'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.FlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('FlexibleKFFittingSmoother'),
    standardFitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    looperFitter = cms.string('LooperFittingSmoother')
)


process.GlbMuKFFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('GlbMuKFFitter'),
    Estimator = cms.string('Chi2EstimatorForMuRefit'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    minHits = cms.int32(3)
)


process.GlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('GlobalDetLayerGeometry')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.GroupedCkfTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('GroupedCkfTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.GroupedCkfTrajectoryBuilderP5 = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('ckfBaseTrajectoryFilterP5'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('GroupedCkfTrajectoryBuilderP5'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.GroupedCkfTrajectoryBuilderP5Bottom = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('ckfBaseTrajectoryFilterP5'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('GroupedCkfTrajectoryBuilderP5Bottom'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string('MeasurementTrackerBottom'),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.GroupedCkfTrajectoryBuilderP5Top = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('ckfBaseTrajectoryFilterP5'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('GroupedCkfTrajectoryBuilderP5Top'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string('MeasurementTrackerTop'),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.HcalHardcodeGeometryEP = cms.ESProducer("HcalHardcodeGeometryEP")


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP")


process.KFFitterForRefitInsideOut = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('KFFitterForRefitInsideOut'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    minHits = cms.int32(3)
)


process.KFFitterForRefitOutsideIn = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('KFFitterForRefitOutsideIn'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
    minHits = cms.int32(3)
)


process.KFFittingSmootheForSTA = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('KFFitterSTA'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('KFSmootherSTA'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFitterSmootherSTA'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.KFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('KFFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('KFSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.KFFittingSmootherBeamHalo = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('KFFitterBH'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('KFSmootherBH'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherBH'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.KFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('RKFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('RKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.KFSmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmootherForMuonTrackLoader'),
    Estimator = cms.string('Chi2EstimatorForMuonTrackLoader'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFSmootherForMuonTrackLoaderL3 = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmootherForMuonTrackLoaderL3'),
    Estimator = cms.string('Chi2EstimatorForMuonTrackLoader'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFSmootherForRefitInsideOut = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmootherForRefitInsideOut'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFSmootherForRefitOutsideIn = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmootherForRefitOutsideIn'),
    Estimator = cms.string('Chi2EstimatorForRefit'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFSwitching1DUpdatorESProducer = cms.ESProducer("KFSwitching1DUpdatorESProducer",
    ComponentName = cms.string('KFSwitching1DUpdator'),
    doEndCap = cms.bool(False)
)


process.KFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('KFFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterial'),
    minHits = cms.int32(3)
)


process.KFTrajectoryFitterBeamHalo = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('KFFitterBH'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    minHits = cms.int32(3)
)


process.KFTrajectoryFitterForSTA = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('KFFitterSTA'),
    Estimator = cms.string('Chi2STA'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SteppingHelixPropagatorAny'),
    minHits = cms.int32(3)
)


process.KFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFTrajectorySmootherBeamHalo = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmootherBH'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFTrajectorySmootherForSTA = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmootherSTA'),
    Estimator = cms.string('Chi2STA'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('SteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFUpdatorESProducer = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('KFUpdator')
)


process.LooperFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('LooperFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('LooperSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('LooperFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.LooperTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('LooperFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    minHits = cms.int32(3)
)


process.LooperTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('LooperSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.MeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(cms.InputTag("siPixelDigis")),
    PixelCPE = cms.string('PixelCPEGeneric'),
    stripLazyGetterProducer = cms.string(''),
    OnDemand = cms.bool(False),
    Regional = cms.bool(False),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('siPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag(cms.InputTag("siStripDigis")),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('siStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string(''),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag(""),
    UseStripModuleQualityDB = cms.bool(True)
)


process.MeasurementTrackerBottom = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(cms.InputTag("siPixelDigis")),
    PixelCPE = cms.string('PixelCPEGeneric'),
    stripLazyGetterProducer = cms.string(''),
    OnDemand = cms.bool(False),
    Regional = cms.bool(False),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('siPixelClustersBottom'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag(cms.InputTag("siStripDigis")),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('siStripClustersBottom'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('MeasurementTrackerBottom'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag(""),
    UseStripModuleQualityDB = cms.bool(True)
)


process.MeasurementTrackerTop = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(cms.InputTag("siPixelDigis")),
    PixelCPE = cms.string('PixelCPEGeneric'),
    stripLazyGetterProducer = cms.string(''),
    OnDemand = cms.bool(False),
    Regional = cms.bool(False),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('siPixelClustersTop'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag(cms.InputTag("siStripDigis")),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('siStripClustersTop'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('MeasurementTrackerTop'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag(""),
    UseStripModuleQualityDB = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.MuonTransientTrackingRecHitBuilderESProducer = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('MuonRecHitBuilder')
)


process.OppositeAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnalyticalPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    label = cms.untracked.string('parametrizedField')
)


process.PixelCPEGenericESProducer = cms.ESProducer("PixelCPEGenericESProducer",
    EdgeClusterErrorX = cms.double(50.0),
    DoCosmics = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    TruncatePixelCharge = cms.bool(True),
    size_cutY = cms.double(3.0),
    size_cutX = cms.double(3.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    IrradiationBiasCorrection = cms.bool(False),
    TanLorentzAnglePerTesla = cms.double(0.106),
    inflate_errors = cms.bool(False),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_highY = cms.double(1.0),
    ClusterProbComputationFlag = cms.int32(0),
    EdgeClusterErrorY = cms.double(85.0),
    ComponentName = cms.string('PixelCPEGeneric'),
    eff_charge_cut_lowY = cms.double(0.0),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    Alpha2Order = cms.bool(True)
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    useOldAnalPropLogic = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    ptMin = cms.double(-1),
    MaxDPhi = cms.double(4.0),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForLoopersOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    useOldAnalPropLogic = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialForLoopersOpposite'),
    Mass = cms.double(0.1396),
    ptMin = cms.double(-1),
    MaxDPhi = cms.double(4.0),
    useRungeKutta = cms.bool(False)
)


process.RK1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('RK1DFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('RK1DSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RK1DFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.RK1DTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('RK1DFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFSwitching1DUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.RK1DTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('RK1DSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFSwitching1DUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.RKFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('RKFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('RKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.RKOutliers1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('RK1DFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('RK1DSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKOutliers1DFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.RKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('RKFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.RKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('RKSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    useDDD = cms.untracked.bool(True),
    compatibiltyWith11 = cms.untracked.bool(True)
)


process.RungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('RungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(True)
)


process.RungeKuttaTrackerPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('RungeKuttaTrackerPropagatorOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0)
)


process.SmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('SmartPropagator')
)


process.SmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('SmartPropagatorAny')
)


process.SmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('SmartPropagatorAnyOpposite')
)


process.SmartPropagatorAnyRK = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagator'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('SmartPropagatorAnyRK')
)


process.SmartPropagatorAnyRKOpposite = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagatorOpposite'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('SmartPropagatorAnyRKOpposite')
)


process.SmartPropagatorOpposite = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite'),
    MuonPropagator = cms.string('SteppingHelixPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('SmartPropagatorOpposite')
)


process.SmartPropagatorRK = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagator'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('SmartPropagatorRK')
)


process.SmartPropagatorRKOpposite = cms.ESProducer("SmartPropagatorESProducer",
    Epsilon = cms.double(5.0),
    TrackerPropagator = cms.string('RungeKuttaTrackerPropagatorOpposite'),
    MuonPropagator = cms.string('SteppingHelixPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('SmartPropagatorRKOpposite')
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorAlongNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useTuningForL2Speed = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlongNoError'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(True),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorAnyNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useTuningForL2Speed = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAnyNoError'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(True),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.SteppingHelixPropagatorL2Along = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useTuningForL2Speed = cms.bool(True),
    ComponentName = cms.string('SteppingHelixPropagatorL2Along'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.SteppingHelixPropagatorL2AlongNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useMatVolumes = cms.bool(True),
    ComponentName = cms.string('SteppingHelixPropagatorL2AlongNoError'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(True),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useTuningForL2Speed = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorL2Any = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useTuningForL2Speed = cms.bool(True),
    ComponentName = cms.string('SteppingHelixPropagatorL2Any'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.SteppingHelixPropagatorL2AnyNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useMatVolumes = cms.bool(True),
    ComponentName = cms.string('SteppingHelixPropagatorL2AnyNoError'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(True),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useTuningForL2Speed = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorL2Opposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useTuningForL2Speed = cms.bool(True),
    ComponentName = cms.string('SteppingHelixPropagatorL2Opposite'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.SteppingHelixPropagatorL2OppositeNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useMatVolumes = cms.bool(True),
    ComponentName = cms.string('SteppingHelixPropagatorL2OppositeNoError'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(True),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useTuningForL2Speed = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorOpposite'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorOppositeNoError = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useTuningForL2Speed = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorOppositeNoError'),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(True),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.StraightLinePropagator = cms.ESProducer("StraightLinePropagatorESProducer",
    ComponentName = cms.string('StraightLinePropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.StripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('SimpleStripCPE')
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle')
)


process.TTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPETemplateReco'),
    ComponentName = cms.string('WithAngleAndTemplate')
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    fromDDD = cms.bool(True)
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
    overrideMasterSector = cms.bool(False),
    useParametrizedTrackerField = cms.bool(True),
    label = cms.untracked.string(''),
    version = cms.string('grid_1103l_090322_3_8t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('parametrizedField'),
    geometryVersion = cms.int32(90322),
    cacheLastVolume = cms.untracked.bool(True)
)


process.ZdcHardcodeGeometryEP = cms.ESProducer("ZdcHardcodeGeometryEP")


process.beamHaloNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('BeamHaloNavigationSchool')
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.ckfBaseInOutTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.9),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(999),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        chargeSignificance = cms.double(-1.0),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('ckfBaseInOutTrajectoryFilter')
)


process.ckfBaseTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.9),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(999),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        chargeSignificance = cms.double(-1.0),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('ckfBaseTrajectoryFilter')
)


process.ckfBaseTrajectoryFilterP5 = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.5),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(4),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(3),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        chargeSignificance = cms.double(-1.0),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('ckfBaseTrajectoryFilterP5')
)


process.ckfTrajectoryFilterBeamHaloMuon = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.1),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(3),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(2),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        chargeSignificance = cms.double(-1.0),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(4)
    ),
    ComponentName = cms.string('ckfTrajectoryFilterBeamHaloMuon')
)


process.compositeTrajectoryFilterESProducer = cms.ESProducer("CompositeTrajectoryFilterESProducer",
    filterNames = cms.vstring(),
    ComponentName = cms.string('compositeTrajectoryFilter')
)


process.convCkfTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('convCkfTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('convCkfTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    clustersToSkip = cms.InputTag("convClusters"),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(3),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.convCkfTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.1),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(3),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('convCkfTrajectoryFilter')
)


process.convLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    TOB5 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TOB4 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TIB1 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    TOB6 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TOB1 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    TOB3 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TID3 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(2)
    ),
    TOB2 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    ComponentName = cms.string('convLayerPairs'),
    TEC = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(7),
        minRing = cms.int32(1)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix2+BPix3', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'BPix3+TIB1', 
        'BPix3+TIB2', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TIB1+TIB2', 
        'TIB1+TIB3', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB2+TID2_pos', 
        'TIB2+TID2_neg', 
        'TIB2+TIB3', 
        'TIB2+TIB4', 
        'TIB3+TIB4', 
        'TIB3+TOB1', 
        'TIB3+TID1_pos', 
        'TIB3+TID1_neg', 
        'TIB4+TOB1', 
        'TIB4+TOB2', 
        'TOB1+TOB2', 
        'TOB1+TOB3', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TOB2+TOB3', 
        'TOB2+TOB4', 
        'TOB2+TEC1_pos', 
        'TOB2+TEC1_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC1_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC7_pos+TEC8_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg', 
        'TEC7_neg+TEC8_neg'),
    TID2 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(2)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("convClusters"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TIB2 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    TIB4 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TID1 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(2)
    ),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("convClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB3 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    )
)


process.convStepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(30),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('RKFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('convStepRKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('convStepFitterSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.convStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('convStepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("SkippingLayerCosmicNavigationSchoolESProducer",
    noPXB = cms.bool(False),
    noTID = cms.bool(False),
    noPXF = cms.bool(False),
    noTIB = cms.bool(False),
    ComponentName = cms.string('CosmicNavigationSchool'),
    allSelf = cms.bool(True),
    noTEC = cms.bool(False),
    noTOB = cms.bool(False),
    selfSearch = cms.bool(True)
)


process.detachedTripletStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(9.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('detachedTripletStepChi2Est')
)


process.detachedTripletStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
    ),
    ComponentName = cms.string('detachedTripletStepSeedLayers')
)


process.detachedTripletStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('detachedTripletStepTrajectoryFilter'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    MeasurementTrackerName = cms.string(''),
    maxPtForLooperReconstruction = cms.double(0.7),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    lockHits = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    bestHitOnly = cms.bool(True),
    maxCand = cms.int32(2),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"),
    alwaysUseInvalidHits = cms.bool(False),
    minNrOfHitsForRebuild = cms.int32(5),
    ComponentName = cms.string('detachedTripletStepTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    estimator = cms.string('detachedTripletStepChi2Est'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    requireSeedHitsInRebuild = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.detachedTripletStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.075),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(999),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(3),
        constantValueForLostHitsFractionFilter = cms.double(0.701),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('detachedTripletStepTrajectoryFilter')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    file = cms.untracked.string(''),
    dump = cms.untracked.vstring('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    useDDD = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string('fakeForIdeal'),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(False)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.initialStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(30.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('initialStepChi2Est')
)


process.initialStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('initialStepTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('initialStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    maxPtForLooperReconstruction = cms.double(0.7),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('initialStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.initialStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.2),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(999),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(3),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('initialStepTrajectoryFilter')
)


process.l1GtBoardMaps = cms.ESProducer("L1GtBoardMapsTrivialProducer",
    CableList = cms.vstring('Free', 
        'Free', 
        'Free', 
        'TechTr', 
        'IsoEGQ', 
        'NoIsoEGQ', 
        'CenJetQ', 
        'ForJetQ', 
        'TauJetQ', 
        'ESumsQ', 
        'HfQ', 
        'Free', 
        'Free', 
        'Free', 
        'Free', 
        'Free', 
        'MQF4', 
        'MQF3', 
        'MQB2', 
        'MQB1', 
        'MQF8', 
        'MQF7', 
        'MQB6', 
        'MQB5', 
        'MQF12', 
        'MQF11', 
        'MQB10', 
        'MQB9'),
    ActiveBoardsDaqRecord = cms.vint32(-1, 0, 1, 2, 3, 
        4, 5, 6, 7, 8, 
        -1, -1),
    CableToPsbMap = cms.vint32(0, 0, 0, 0, 1, 
        1, 1, 1, 2, 2, 
        2, 2, 3, 3, 3, 
        3, 4, 4, 4, 4, 
        5, 5, 5, 5, 6, 
        6, 6, 6),
    BoardPositionDaqRecord = cms.vint32(1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        -1, -1),
    BoardPositionEvmRecord = cms.vint32(1, 3, -1, -1, -1, 
        -1, -1, -1, -1, -1, 
        2, -1),
    BoardList = cms.vstring('GTFE', 
        'FDL', 
        'PSB', 
        'PSB', 
        'PSB', 
        'PSB', 
        'PSB', 
        'PSB', 
        'PSB', 
        'GMT', 
        'TCS', 
        'TIM'),
    PsbInput = cms.VPSet(cms.PSet(
        Slot = cms.int32(9),
        Ch0 = cms.vstring('TechTrig'),
        Ch1 = cms.vstring('TechTrig'),
        Ch2 = cms.vstring(),
        Ch3 = cms.vstring(),
        Ch4 = cms.vstring(),
        Ch5 = cms.vstring(),
        Ch6 = cms.vstring(),
        Ch7 = cms.vstring()
    ), 
        cms.PSet(
            Slot = cms.int32(13),
            Ch0 = cms.vstring('ForJet', 
                'ForJet'),
            Ch1 = cms.vstring('ForJet', 
                'ForJet'),
            Ch2 = cms.vstring('CenJet', 
                'CenJet'),
            Ch3 = cms.vstring('CenJet', 
                'CenJet'),
            Ch4 = cms.vstring('NoIsoEG', 
                'NoIsoEG'),
            Ch5 = cms.vstring('NoIsoEG', 
                'NoIsoEG'),
            Ch6 = cms.vstring('IsoEG', 
                'IsoEG'),
            Ch7 = cms.vstring('IsoEG', 
                'IsoEG')
        ), 
        cms.PSet(
            Slot = cms.int32(14),
            Ch0 = cms.vstring(),
            Ch1 = cms.vstring(),
            Ch2 = cms.vstring('HfBitCounts', 
                'HfRingEtSums'),
            Ch3 = cms.vstring(),
            Ch4 = cms.vstring('ETT', 
                'HTT'),
            Ch5 = cms.vstring('ETM', 
                'ETM'),
            Ch6 = cms.vstring('TauJet', 
                'TauJet'),
            Ch7 = cms.vstring('TauJet', 
                'TauJet')
        ), 
        cms.PSet(
            Slot = cms.int32(15),
            Ch0 = cms.vstring(),
            Ch1 = cms.vstring(),
            Ch2 = cms.vstring(),
            Ch3 = cms.vstring(),
            Ch4 = cms.vstring(),
            Ch5 = cms.vstring(),
            Ch6 = cms.vstring(),
            Ch7 = cms.vstring()
        ), 
        cms.PSet(
            Slot = cms.int32(19),
            Ch0 = cms.vstring(),
            Ch1 = cms.vstring(),
            Ch2 = cms.vstring(),
            Ch3 = cms.vstring(),
            Ch4 = cms.vstring(),
            Ch5 = cms.vstring(),
            Ch6 = cms.vstring(),
            Ch7 = cms.vstring()
        ), 
        cms.PSet(
            Slot = cms.int32(20),
            Ch0 = cms.vstring(),
            Ch1 = cms.vstring(),
            Ch2 = cms.vstring(),
            Ch3 = cms.vstring(),
            Ch4 = cms.vstring(),
            Ch5 = cms.vstring(),
            Ch6 = cms.vstring(),
            Ch7 = cms.vstring()
        ), 
        cms.PSet(
            Slot = cms.int32(21),
            Ch0 = cms.vstring(),
            Ch1 = cms.vstring(),
            Ch2 = cms.vstring(),
            Ch3 = cms.vstring(),
            Ch4 = cms.vstring(),
            Ch5 = cms.vstring(),
            Ch6 = cms.vstring(),
            Ch7 = cms.vstring()
        )),
    BoardHexNameMap = cms.vint32(0, 253, 187, 187, 187, 
        187, 187, 187, 187, 221, 
        204, 173),
    ActiveBoardsEvmRecord = cms.vint32(-1, 1, -1, -1, -1, 
        -1, -1, -1, -1, -1, 
        0, -1),
    BoardSlotMap = cms.vint32(17, 10, 9, 13, 14, 
        15, 19, 20, 21, 18, 
        7, 16),
    BoardIndex = cms.vint32(0, 0, 0, 1, 2, 
        3, 4, 5, 6, 0, 
        0, 0)
)


process.l1GtParameters = cms.ESProducer("L1GtParametersTrivialProducer",
    EvmActiveBoards = cms.uint32(65535),
    DaqNrBxBoard = cms.vint32(3, 3, 3, 3, 3, 
        3, 3, 3, 3),
    DaqActiveBoards = cms.uint32(65535),
    TotalBxInEvent = cms.int32(3),
    EvmNrBxBoard = cms.vint32(1, 3),
    BstLengthBytes = cms.uint32(30)
)


process.l1GtPrescaleFactorsAlgoTrig = cms.ESProducer("L1GtPrescaleFactorsAlgoTrigTrivialProducer",
    PrescaleFactorsSet = cms.VPSet(cms.PSet(
        PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1)
    ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1)
        ))
)


process.l1GtPrescaleFactorsTechTrig = cms.ESProducer("L1GtPrescaleFactorsTechTrigTrivialProducer",
    PrescaleFactorsSet = cms.VPSet(cms.PSet(
        PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1)
    ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ), 
        cms.PSet(
            PrescaleFactors = cms.vint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1)
        ))
)


process.l1GtPsbSetup = cms.ESProducer("L1GtPsbSetupTrivialProducer",
    PsbSetup = cms.VPSet(cms.PSet(
        Slot = cms.int32(9),
        Ch1SendLvds = cms.bool(True),
        Ch0SendLvds = cms.bool(True),
        EnableRecSerLink = cms.vuint32(0, 0, 0, 0, 0, 
            0, 0, 0),
        EnableRecLvds = cms.vuint32(1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1, 1, 1, 1, 1, 
            1)
    ), 
        cms.PSet(
            Slot = cms.int32(13),
            Ch1SendLvds = cms.bool(False),
            Ch0SendLvds = cms.bool(False),
            EnableRecSerLink = cms.vuint32(1, 1, 1, 1, 1, 
                1, 1, 1),
            EnableRecLvds = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0)
        ), 
        cms.PSet(
            Slot = cms.int32(14),
            Ch1SendLvds = cms.bool(False),
            Ch0SendLvds = cms.bool(False),
            EnableRecSerLink = cms.vuint32(1, 1, 1, 1, 1, 
                1, 1, 1),
            EnableRecLvds = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0)
        ), 
        cms.PSet(
            Slot = cms.int32(15),
            Ch1SendLvds = cms.bool(True),
            Ch0SendLvds = cms.bool(True),
            EnableRecSerLink = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0),
            EnableRecLvds = cms.vuint32(1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 
                1)
        ), 
        cms.PSet(
            Slot = cms.int32(19),
            Ch1SendLvds = cms.bool(False),
            Ch0SendLvds = cms.bool(False),
            EnableRecSerLink = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0),
            EnableRecLvds = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0)
        ), 
        cms.PSet(
            Slot = cms.int32(20),
            Ch1SendLvds = cms.bool(False),
            Ch0SendLvds = cms.bool(False),
            EnableRecSerLink = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0),
            EnableRecLvds = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0)
        ), 
        cms.PSet(
            Slot = cms.int32(21),
            Ch1SendLvds = cms.bool(False),
            Ch0SendLvds = cms.bool(False),
            EnableRecSerLink = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0),
            EnableRecLvds = cms.vuint32(0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 
                0)
        ))
)


process.l1GtStableParameters = cms.ESProducer("L1GtStableParametersTrivialProducer",
    NumberL1IsoEG = cms.uint32(4),
    NumberL1JetCounts = cms.uint32(12),
    UnitLength = cms.int32(8),
    NumberL1ForJet = cms.uint32(4),
    IfCaloEtaNumberBits = cms.uint32(4),
    IfMuEtaNumberBits = cms.uint32(6),
    NumberL1TauJet = cms.uint32(4),
    NumberPsbBoards = cms.int32(7),
    NumberConditionChips = cms.uint32(2),
    NumberL1Mu = cms.uint32(4),
    NumberL1CenJet = cms.uint32(4),
    NumberPhysTriggers = cms.uint32(128),
    PinsOnConditionChip = cms.uint32(96),
    NumberTechnicalTriggers = cms.uint32(64),
    OrderConditionChip = cms.vint32(2, 1),
    NumberPhysTriggersExtended = cms.uint32(64),
    WordLength = cms.int32(64),
    NumberL1NoIsoEG = cms.uint32(4)
)


process.l1GtTriggerMaskAlgoTrig = cms.ESProducer("L1GtTriggerMaskAlgoTrigTrivialProducer",
    TriggerMask = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0)
)


process.l1GtTriggerMaskTechTrig = cms.ESProducer("L1GtTriggerMaskTechTrigTrivialProducer",
    TriggerMask = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0)
)


process.l1GtTriggerMaskVetoAlgoTrig = cms.ESProducer("L1GtTriggerMaskVetoAlgoTrigTrivialProducer",
    TriggerMask = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0)
)


process.l1GtTriggerMaskVetoTechTrig = cms.ESProducer("L1GtTriggerMaskVetoTechTrigTrivialProducer",
    TriggerMask = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0)
)


process.l1GtTriggerMenuXml = cms.ESProducer("L1GtTriggerMenuXmlProducer",
    VmeXmlFile = cms.string(''),
    DefXmlFile = cms.string('L1Menu_Commissioning2009_v1_L1T_Scales_20080926_startup_Imp0.xml'),
    TriggerMenuLuminosity = cms.string('startup')
)


process.lowPtTripletStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(9.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('lowPtTripletStepChi2Est')
)


process.lowPtTripletStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
    ),
    ComponentName = cms.string('lowPtTripletStepSeedLayers')
)


process.lowPtTripletStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('lowPtTripletStepTrajectoryFilter'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    MeasurementTrackerName = cms.string(''),
    maxPtForLooperReconstruction = cms.double(0.7),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    lockHits = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    bestHitOnly = cms.bool(True),
    maxCand = cms.int32(3),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"),
    alwaysUseInvalidHits = cms.bool(True),
    minNrOfHitsForRebuild = cms.int32(5),
    ComponentName = cms.string('lowPtTripletStepTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    estimator = cms.string('lowPtTripletStepChi2Est'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    requireSeedHitsInRebuild = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.lowPtTripletStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.075),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(999),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(3),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('lowPtTripletStepTrajectoryFilter')
)


process.mixedTripletStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('mixedTripletStepChi2Est')
)


process.mixedTripletStepPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('mixedTripletStepPropagator'),
    Mass = cms.double(0.105),
    ptMin = cms.double(0.1),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('mixedTripletStepPropagatorOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(0.1),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepSeedLayersA = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix2_pos+TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC2_neg+TEC3_neg'),
    TEC = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        maxRing = cms.int32(1)
    ),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    ComponentName = cms.string('mixedTripletStepSeedLayersA')
)


process.mixedTripletStepSeedLayersB = cms.ESProducer("SeedingLayersESProducer",
    ComponentName = cms.string('mixedTripletStepSeedLayersB'),
    layerList = cms.vstring('BPix2+BPix3+TIB1', 
        'BPix2+BPix3+TIB2'),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)


process.mixedTripletStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('mixedTripletStepPropagator'),
    trajectoryFilterName = cms.string('mixedTripletStepTrajectoryFilter'),
    propagatorOpposite = cms.string('mixedTripletStepPropagatorOpposite'),
    MeasurementTrackerName = cms.string(''),
    maxPtForLooperReconstruction = cms.double(0.7),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    lockHits = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    bestHitOnly = cms.bool(True),
    maxCand = cms.int32(2),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"),
    alwaysUseInvalidHits = cms.bool(True),
    minNrOfHitsForRebuild = cms.int32(5),
    ComponentName = cms.string('mixedTripletStepTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    estimator = cms.string('mixedTripletStepChi2Est'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    requireSeedHitsInRebuild = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.mixedTripletStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.1),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(3),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('mixedTripletStepTrajectoryFilter')
)


process.mixedlayerpairs = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix2_pos+TEC1_pos', 
        'FPix2_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC1_neg', 
        'FPix2_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'),
    TEC = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    ComponentName = cms.string('MixedLayerPairs')
)


process.mixedlayertriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix1+BPix2+TIB1', 
        'BPix1+BPix3+TIB1', 
        'BPix2+BPix3+TIB1', 
        'BPix1+FPix1_pos+TID1_pos', 
        'BPix1+FPix1_neg+TID1_neg', 
        'BPix1+FPix1_pos+TID2_pos', 
        'BPix1+FPix1_neg+TID2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix1_pos+FPix2_pos+TEC2_pos', 
        'FPix1_neg+FPix2_neg+TEC2_neg'),
    ComponentName = cms.string('MixedLayerTriplets'),
    TEC = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TID = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.125),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.myTTRHBuilderWithoutAngle4MixedPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedPairs')
)


process.myTTRHBuilderWithoutAngle4MixedTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedTriplets')
)


process.myTTRHBuilderWithoutAngle4PixelPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelPairs')
)


process.myTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelTriplets')
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool')
)


process.pixelLessLayerPairs4PixelLessTracking = cms.ESProducer("SeedingLayersESProducer",
    TIB3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched")
    ),
    TIB2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched")
    ),
    TIB1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched")
    ),
    TID1 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1)
    ),
    TID3 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1)
    ),
    TID2 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1)
    ),
    ComponentName = cms.string('pixelLessLayerPairs4PixelLessTracking'),
    TEC = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(2),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched")
    ),
    layerList = cms.vstring('TIB1+TIB2', 
        'TIB1+TIB3', 
        'TIB2+TIB3', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg')
)


process.pixelLessStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('pixelLessStepChi2Est')
)


process.pixelLessStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    TID = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        maxRing = cms.int32(2)
    ),
    ComponentName = cms.string('pixelLessStepSeedLayers'),
    layerList = cms.vstring('TIB1+TIB2', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC3_pos+TEC5_pos', 
        'TEC4_pos+TEC5_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC3_neg+TEC5_neg', 
        'TEC4_neg+TEC5_neg'),
    TEC = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        maxRing = cms.int32(2)
    ),
    TIB = cms.PSet(
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)


process.pixelLessStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('pixelLessStepTrajectoryFilter'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    MeasurementTrackerName = cms.string(''),
    maxPtForLooperReconstruction = cms.double(0.7),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    lockHits = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    bestHitOnly = cms.bool(True),
    maxCand = cms.int32(2),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"),
    alwaysUseInvalidHits = cms.bool(False),
    minNrOfHitsForRebuild = cms.int32(4),
    ComponentName = cms.string('pixelLessStepTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    estimator = cms.string('pixelLessStepChi2Est'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    requireSeedHitsInRebuild = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.pixelLessStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.1),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(4),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('pixelLessStepTrajectoryFilter')
)


process.pixelPairElectronSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("tripletElectronClusterMask"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("tripletElectronClusterMask"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    ComponentName = cms.string('pixelPairElectronSeedLayers')
)


process.pixelPairStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(9.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('pixelPairStepChi2Est')
)


process.pixelPairStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("pixelPairStepClusters"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("pixelPairStepClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    ComponentName = cms.string('pixelPairStepSeedLayers')
)


process.pixelPairStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('pixelPairStepTrajectoryFilter'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    MeasurementTrackerName = cms.string(''),
    maxPtForLooperReconstruction = cms.double(0.7),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    lockHits = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    bestHitOnly = cms.bool(True),
    maxCand = cms.int32(2),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"),
    alwaysUseInvalidHits = cms.bool(True),
    minNrOfHitsForRebuild = cms.int32(5),
    ComponentName = cms.string('pixelPairStepTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    estimator = cms.string('pixelPairStepChi2Est'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    requireSeedHitsInRebuild = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.pixelPairStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.1),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(999),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(3),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('pixelPairStepTrajectoryFilter')
)


process.pixellayerpairs = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    ComponentName = cms.string('PixelLayerPairs')
)


process.pixellayertriplets = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    ComponentName = cms.string('PixelLayerTriplets')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.rings = cms.ESProducer("RingMakerESProducer",
    DumpDetIds = cms.untracked.bool(False),
    ComponentName = cms.string(''),
    RingAsciiFileName = cms.untracked.string('rings.dat'),
    DetIdsDumpFileName = cms.untracked.string('tracker_detids.dat'),
    WriteOutRingsToAsciiFile = cms.untracked.bool(False),
    Configuration = cms.untracked.string('FULL')
)


process.ringsP5 = cms.ESProducer("RingMakerESProducer",
    DumpDetIds = cms.untracked.bool(False),
    ComponentName = cms.string('P5'),
    RingAsciiFileName = cms.untracked.string('rings_p5.dat'),
    DetIdsDumpFileName = cms.untracked.string('tracker_detids.dat'),
    WriteOutRingsToAsciiFile = cms.untracked.bool(False),
    Configuration = cms.untracked.string('P5')
)


process.roads = cms.ESProducer("RoadMapMakerESProducer",
    GeometryStructure = cms.string('FullDetector'),
    ComponentName = cms.string(''),
    RingsLabel = cms.string(''),
    WriteOutRoadMapToAsciiFile = cms.untracked.bool(False),
    SeedingType = cms.string('FourRingSeeds'),
    RoadMapAsciiFile = cms.untracked.string('roads.dat')
)


process.roadsP5 = cms.ESProducer("RoadMapMakerESProducer",
    GeometryStructure = cms.string('P5'),
    ComponentName = cms.string('P5'),
    RingsLabel = cms.string('P5'),
    WriteOutRoadMapToAsciiFile = cms.untracked.bool(False),
    SeedingType = cms.string('TwoRingSeeds'),
    RoadMapAsciiFile = cms.untracked.string('roads.dat')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    printDebug = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    APVGain = cms.VPSet(cms.PSet(
        Record = cms.string('SiStripApvGainRcd'),
        NormalizationFactor = cms.untracked.double(1.0),
        Label = cms.untracked.string('')
    ), 
        cms.PSet(
            Record = cms.string('SiStripApvGain2Rcd'),
            NormalizationFactor = cms.untracked.double(1.0),
            Label = cms.untracked.string('')
        )),
    AutomaticNormalization = cms.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        record = cms.string('SiStripLatencyRcd'),
        label = cms.untracked.string('')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('deconvolution')
    ),
    LorentzAnglePeakMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('peak')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    appendToDataLabel = cms.string(''),
    PrintDebugOutput = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        ))
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripPairElectronSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    TID = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("tripletElectronClusterMask"),
        maxRing = cms.int32(2)
    ),
    ComponentName = cms.string('stripPairElectronSeedLayers'),
    layerList = cms.vstring('TIB1+TIB2', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TID2_pos+TID3_pos', 
        'TID2_neg+TID3_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC3_pos+TEC5_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC3_neg+TEC5_neg'),
    TEC = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("tripletElectronClusterMask"),
        maxRing = cms.int32(2)
    ),
    TIB = cms.PSet(
        skipClusters = cms.InputTag("tripletElectronClusterMask"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)


process.templates = cms.ESProducer("PixelCPETemplateRecoESProducer",
    DoCosmics = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    ComponentName = cms.string('PixelCPETemplateReco'),
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    speed = cms.int32(-2),
    UseClusterSplitter = cms.bool(False)
)


process.tobTecFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('tobTecFlexibleKFFittingSmoother'),
    standardFitter = cms.string('tobTecStepFitterSmoother'),
    looperFitter = cms.string('tobTecStepFitterSmootherForLoopers')
)


process.tobTecStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('tobTecStepChi2Est')
)


process.tobTecStepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(30),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('tobTecStepRKFitter'),
    MinNumberOfHits = cms.int32(8),
    Smoother = cms.string('tobTecStepRKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('tobTecStepFitterSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.tobTecStepFitterSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(30),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('tobTecStepRKFitterForLoopers'),
    MinNumberOfHits = cms.int32(8),
    Smoother = cms.string('tobTecStepRKSmootherForLoopers'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('tobTecStepFitterSmootherForLoopers'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.tobTecStepInOutTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.1),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(4),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('tobTecStepInOutTrajectoryFilter')
)


process.tobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('tobTecStepRKFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    minHits = cms.int32(8)
)


process.tobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('tobTecStepRKFitterForLoopers'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    minHits = cms.int32(8)
)


process.tobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(8),
    ComponentName = cms.string('tobTecStepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.tobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(8),
    ComponentName = cms.string('tobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.tobTecStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    TOB = cms.PSet(
        skipClusters = cms.InputTag("tobTecStepClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    ComponentName = cms.string('tobTecStepSeedLayers'),
    layerList = cms.vstring('TOB1+TOB2', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg'),
    TEC = cms.PSet(
        minRing = cms.int32(5),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        maxRing = cms.int32(5)
    )
)


process.tobTecStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('tobTecStepTrajectoryFilter'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    MeasurementTrackerName = cms.string(''),
    maxPtForLooperReconstruction = cms.double(0.7),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    lockHits = cms.bool(True),
    useSameTrajFilter = cms.bool(False),
    bestHitOnly = cms.bool(True),
    maxCand = cms.int32(2),
    clustersToSkip = cms.InputTag("tobTecStepClusters"),
    alwaysUseInvalidHits = cms.bool(False),
    minNrOfHitsForRebuild = cms.int32(4),
    ComponentName = cms.string('tobTecStepTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    inOutTrajectoryFilterName = cms.string('tobTecStepInOutTrajectoryFilter'),
    estimator = cms.string('tobTecStepChi2Est'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    requireSeedHitsInRebuild = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.tobTecStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
        minPt = cms.double(0.1),
        minNumberOfHits = cms.int32(13),
        minHitsMinPt = cms.int32(3),
        maxLostHitsFraction = cms.double(0.1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minNumberOfHitsPerLoop = cms.int32(4),
        minimumNumberOfHits = cms.int32(6),
        constantValueForLostHitsFractionFilter = cms.double(1.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('tobTecStepTrajectoryFilter')
)


process.trajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('TrajectoryCleanerBySharedHits'),
    fractionShared = cms.double(0.19),
    ValidHitBonus = cms.double(5.0),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    allowSharedFirstHit = cms.bool(True)
)


process.tripletElectronSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        skipClusters = cms.InputTag("pixelLessStepSeedClusterMask"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    ComponentName = cms.string('tripletElectronSeedLayers')
)


process.ttrhbwor = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('Fake'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('Fake'),
    ComponentName = cms.string('WithoutRefit')
)


process.ttrhbwr = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('WithTrackAngle')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDeDxMip_3D_Rcd'),
        tag = cms.string('Data7TeV_Deco_3D_Rcd_38X'),
        connect = cms.untracked.string('sqlite_file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data7TeV_Deco_SiStripDeDxMip_3D_Rcd.db')
    )),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    globaltag = cms.string('FT53_V21A_AN6::All')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.L1GtBoardMapsRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtBoardMapsRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtParametersRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtParametersRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtPrescaleFactorsAlgoTrigRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtPrescaleFactorsAlgoTrigRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtPrescaleFactorsTechTrigRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtPrescaleFactorsTechTrigRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtPsbSetupRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtPsbSetupRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtStableParametersRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtStableParametersRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtTriggerMaskAlgoTrigRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMaskAlgoTrigRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtTriggerMaskTechTrigRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMaskTechTrigRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtTriggerMaskVetoAlgoTrigRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMaskVetoAlgoTrigRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtTriggerMaskVetoTechTrigRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMaskVetoTechTrigRcd'),
    firstValid = cms.vuint32(1)
)


process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMenuRcd'),
    firstValid = cms.vuint32(1)
)


process.XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/CMSCommonData/data/cmsTracker.xml', 
        'Geometry/CMSCommonData/data/caloBase.xml', 
        'Geometry/CMSCommonData/data/cmsCalo.xml', 
        'Geometry/CMSCommonData/data/muonBase.xml', 
        'Geometry/CMSCommonData/data/cmsMuon.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/CMSCommonData/data/beampipe.xml', 
        'Geometry/CMSCommonData/data/cmsBeam.xml', 
        'Geometry/CMSCommonData/data/muonMB.xml', 
        'Geometry/CMSCommonData/data/muonMagnet.xml', 
        'Geometry/TrackerCommonData/data/pixfwdMaterials.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x2.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x3.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x4.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanelBase.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanel.xml', 
        'Geometry/TrackerCommonData/data/pixfwdBlade.xml', 
        'Geometry/TrackerCommonData/data/pixfwdNipple.xml', 
        'Geometry/TrackerCommonData/data/pixfwdDisk.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCylinder.xml', 
        'Geometry/TrackerCommonData/data/pixfwd.xml', 
        'Geometry/TrackerCommonData/data/pixbarmaterial.xml', 
        'Geometry/TrackerCommonData/data/pixbarladder.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderfull.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderhalf.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer0.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer1.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer2.xml', 
        'Geometry/TrackerCommonData/data/pixbar.xml', 
        'Geometry/TrackerCommonData/data/tibtidcommonmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmodpar.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0a.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0b.xml', 
        'Geometry/TrackerCommonData/data/tibmodule2.xml', 
        'Geometry/TrackerCommonData/data/tibstringpar.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring0lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring0.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring1lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring1.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring2lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring2.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring3lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring3.xml', 
        'Geometry/TrackerCommonData/data/tiblayerpar.xml', 
        'Geometry/TrackerCommonData/data/tiblayer0.xml', 
        'Geometry/TrackerCommonData/data/tiblayer1.xml', 
        'Geometry/TrackerCommonData/data/tiblayer2.xml', 
        'Geometry/TrackerCommonData/data/tiblayer3.xml', 
        'Geometry/TrackerCommonData/data/tib.xml', 
        'Geometry/TrackerCommonData/data/tidmaterial.xml', 
        'Geometry/TrackerCommonData/data/tidmodpar.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule2.xml', 
        'Geometry/TrackerCommonData/data/tidringpar.xml', 
        'Geometry/TrackerCommonData/data/tidring0.xml', 
        'Geometry/TrackerCommonData/data/tidring0f.xml', 
        'Geometry/TrackerCommonData/data/tidring0b.xml', 
        'Geometry/TrackerCommonData/data/tidring1.xml', 
        'Geometry/TrackerCommonData/data/tidring1f.xml', 
        'Geometry/TrackerCommonData/data/tidring1b.xml', 
        'Geometry/TrackerCommonData/data/tidring2.xml', 
        'Geometry/TrackerCommonData/data/tid.xml', 
        'Geometry/TrackerCommonData/data/tidf.xml', 
        'Geometry/TrackerCommonData/data/tidb.xml', 
        'Geometry/TrackerCommonData/data/tibtidservices.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesf.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesb.xml', 
        'Geometry/TrackerCommonData/data/tobmaterial.xml', 
        'Geometry/TrackerCommonData/data/tobmodpar.xml', 
        'Geometry/TrackerCommonData/data/tobmodule0.xml', 
        'Geometry/TrackerCommonData/data/tobmodule2.xml', 
        'Geometry/TrackerCommonData/data/tobmodule4.xml', 
        'Geometry/TrackerCommonData/data/tobrodpar.xml', 
        'Geometry/TrackerCommonData/data/tobrod0c.xml', 
        'Geometry/TrackerCommonData/data/tobrod0l.xml', 
        'Geometry/TrackerCommonData/data/tobrod0h.xml', 
        'Geometry/TrackerCommonData/data/tobrod0.xml', 
        'Geometry/TrackerCommonData/data/tobrod1l.xml', 
        'Geometry/TrackerCommonData/data/tobrod1h.xml', 
        'Geometry/TrackerCommonData/data/tobrod1.xml', 
        'Geometry/TrackerCommonData/data/tobrod2c.xml', 
        'Geometry/TrackerCommonData/data/tobrod2l.xml', 
        'Geometry/TrackerCommonData/data/tobrod2h.xml', 
        'Geometry/TrackerCommonData/data/tobrod2.xml', 
        'Geometry/TrackerCommonData/data/tobrod3l.xml', 
        'Geometry/TrackerCommonData/data/tobrod3h.xml', 
        'Geometry/TrackerCommonData/data/tobrod3.xml', 
        'Geometry/TrackerCommonData/data/tobrod4c.xml', 
        'Geometry/TrackerCommonData/data/tobrod4l.xml', 
        'Geometry/TrackerCommonData/data/tobrod4h.xml', 
        'Geometry/TrackerCommonData/data/tobrod4.xml', 
        'Geometry/TrackerCommonData/data/tobrod5l.xml', 
        'Geometry/TrackerCommonData/data/tobrod5h.xml', 
        'Geometry/TrackerCommonData/data/tobrod5.xml', 
        'Geometry/TrackerCommonData/data/tob.xml', 
        'Geometry/TrackerCommonData/data/tecmaterial.xml', 
        'Geometry/TrackerCommonData/data/tecmodpar.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule2.xml', 
        'Geometry/TrackerCommonData/data/tecmodule3.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule5.xml', 
        'Geometry/TrackerCommonData/data/tecmodule6.xml', 
        'Geometry/TrackerCommonData/data/tecpetpar.xml', 
        'Geometry/TrackerCommonData/data/tecring0.xml', 
        'Geometry/TrackerCommonData/data/tecring1.xml', 
        'Geometry/TrackerCommonData/data/tecring2.xml', 
        'Geometry/TrackerCommonData/data/tecring3.xml', 
        'Geometry/TrackerCommonData/data/tecring4.xml', 
        'Geometry/TrackerCommonData/data/tecring5.xml', 
        'Geometry/TrackerCommonData/data/tecring6.xml', 
        'Geometry/TrackerCommonData/data/tecring0f.xml', 
        'Geometry/TrackerCommonData/data/tecring1f.xml', 
        'Geometry/TrackerCommonData/data/tecring2f.xml', 
        'Geometry/TrackerCommonData/data/tecring3f.xml', 
        'Geometry/TrackerCommonData/data/tecring4f.xml', 
        'Geometry/TrackerCommonData/data/tecring5f.xml', 
        'Geometry/TrackerCommonData/data/tecring6f.xml', 
        'Geometry/TrackerCommonData/data/tecring0b.xml', 
        'Geometry/TrackerCommonData/data/tecring1b.xml', 
        'Geometry/TrackerCommonData/data/tecring2b.xml', 
        'Geometry/TrackerCommonData/data/tecring3b.xml', 
        'Geometry/TrackerCommonData/data/tecring4b.xml', 
        'Geometry/TrackerCommonData/data/tecring5b.xml', 
        'Geometry/TrackerCommonData/data/tecring6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetalf.xml', 
        'Geometry/TrackerCommonData/data/tecpetalb.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8b.xml', 
        'Geometry/TrackerCommonData/data/tecwheel.xml', 
        'Geometry/TrackerCommonData/data/tecwheela.xml', 
        'Geometry/TrackerCommonData/data/tecwheelb.xml', 
        'Geometry/TrackerCommonData/data/tecwheelc.xml', 
        'Geometry/TrackerCommonData/data/tecwheeld.xml', 
        'Geometry/TrackerCommonData/data/tecwheel6.xml', 
        'Geometry/TrackerCommonData/data/tecservices.xml', 
        'Geometry/TrackerCommonData/data/tecbackplate.xml', 
        'Geometry/TrackerCommonData/data/tec.xml', 
        'Geometry/TrackerCommonData/data/trackermaterial.xml', 
        'Geometry/TrackerCommonData/data/tracker.xml', 
        'Geometry/TrackerCommonData/data/trackerpixbar.xml', 
        'Geometry/TrackerCommonData/data/trackerpixfwd.xml', 
        'Geometry/TrackerCommonData/data/trackertibtidservices.xml', 
        'Geometry/TrackerCommonData/data/trackertib.xml', 
        'Geometry/TrackerCommonData/data/trackertid.xml', 
        'Geometry/TrackerCommonData/data/trackertob.xml', 
        'Geometry/TrackerCommonData/data/trackertec.xml', 
        'Geometry/TrackerCommonData/data/trackerbulkhead.xml', 
        'Geometry/TrackerCommonData/data/trackerother.xml', 
        'Geometry/EcalCommonData/data/eregalgo.xml', 
        'Geometry/EcalCommonData/data/ebalgo.xml', 
        'Geometry/EcalCommonData/data/ebcon.xml', 
        'Geometry/EcalCommonData/data/ebrot.xml', 
        'Geometry/EcalCommonData/data/eecon.xml', 
        'Geometry/EcalCommonData/data/eefixed.xml', 
        'Geometry/EcalCommonData/data/eehier.xml', 
        'Geometry/EcalCommonData/data/eealgo.xml', 
        'Geometry/EcalCommonData/data/escon.xml', 
        'Geometry/EcalCommonData/data/esalgo.xml', 
        'Geometry/EcalCommonData/data/eeF.xml', 
        'Geometry/EcalCommonData/data/eeB.xml', 
        'Geometry/HcalCommonData/data/hcalrotations.xml', 
        'Geometry/HcalCommonData/data/hcalalgo.xml', 
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml', 
        'Geometry/HcalCommonData/data/hcalendcapalgo.xml', 
        'Geometry/HcalCommonData/data/hcalouteralgo.xml', 
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml', 
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml', 
        'Geometry/MuonCommonData/data/mbCommon.xml', 
        'Geometry/MuonCommonData/data/mb1.xml', 
        'Geometry/MuonCommonData/data/mb2.xml', 
        'Geometry/MuonCommonData/data/mb3.xml', 
        'Geometry/MuonCommonData/data/mb4.xml', 
        'Geometry/MuonCommonData/data/muonYoke.xml', 
        'Geometry/MuonCommonData/data/mf.xml', 
        'Geometry/ForwardCommonData/data/forward.xml', 
        'Geometry/ForwardCommonData/data/bundle/forwardshield.xml', 
        'Geometry/ForwardCommonData/data/brmrotations.xml', 
        'Geometry/ForwardCommonData/data/brm.xml', 
        'Geometry/ForwardCommonData/data/totemMaterials.xml', 
        'Geometry/ForwardCommonData/data/totemRotations.xml', 
        'Geometry/ForwardCommonData/data/totemt1.xml', 
        'Geometry/ForwardCommonData/data/totemt2.xml', 
        'Geometry/ForwardCommonData/data/ionpump.xml', 
        'Geometry/MuonCommonData/data/muonNumbering.xml', 
        'Geometry/TrackerCommonData/data/trackerStructureTopology.xml', 
        'Geometry/TrackerSimData/data/trackersens.xml', 
        'Geometry/TrackerRecoData/data/trackerRecoMaterial.xml', 
        'Geometry/EcalSimData/data/ecalsens.xml', 
        'Geometry/HcalCommonData/data/hcalsenspmf.xml', 
        'Geometry/HcalSimData/data/hf.xml', 
        'Geometry/HcalSimData/data/hfpmt.xml', 
        'Geometry/HcalSimData/data/hffibrebundle.xml', 
        'Geometry/HcalSimData/data/CaloUtil.xml', 
        'Geometry/MuonSimData/data/muonSens.xml', 
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml', 
        'Geometry/RPCGeometryBuilder/data/RPCSpecs.xml', 
        'Geometry/ForwardCommonData/data/brmsens.xml', 
        'Geometry/HcalSimData/data/HcalProdCuts.xml', 
        'Geometry/EcalSimData/data/EcalProdCuts.xml', 
        'Geometry/EcalSimData/data/ESProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml', 
        'Geometry/MuonSimData/data/muonProdCuts.xml', 
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml', 
        'Geometry/CMSCommonData/data/FieldParameters.xml'),
    rootNodeName = cms.string('cms:OCMS')
)


process.eegeom = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd'),
    firstValid = cms.vuint32(1)
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('GainWidths')
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml', 
        'Geometry/CMSCommonData/data/materials.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.prefer("magfield")

process.CSCTimingExtractorBlock = cms.PSet(
    CSCTimingParameters = cms.PSet(
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTsegments = cms.InputTag("dt4DSegments"),
            DTradius = cms.double(0.01),
            TightMatchDT = cms.bool(False),
            TightMatchCSC = cms.bool(True)
        ),
        CSCsegments = cms.InputTag("csc2DSegments"),
        CSCStripTimeOffset = cms.double(0.0),
        CSCStripError = cms.double(7.0),
        UseStripTime = cms.bool(True),
        debug = cms.bool(False),
        CSCWireError = cms.double(8.6),
        CSCWireTimeOffset = cms.double(0.0),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                'PropagatorWithMaterial', 
                'PropagatorWithMaterialOpposite'),
            RPCLayers = cms.bool(True)
        ),
        PruneCut = cms.double(9.0),
        UseWireTime = cms.bool(True)
    )
)

process.ChargeSignificanceTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ChargeSignificanceTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0)
)

process.CkfBaseTrajectoryFilter_block = cms.PSet(
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minNumberOfHits = cms.int32(13),
    minHitsMinPt = cms.int32(3),
    maxLostHitsFraction = cms.double(0.1),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(999),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minNumberOfHitsPerLoop = cms.int32(4),
    minimumNumberOfHits = cms.int32(5),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    chargeSignificance = cms.double(-1.0)
)

process.CompositeTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet()
)

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10)
    )
)

process.DTLinearDriftFromDBAlgo = cms.PSet(
    recAlgoConfig = cms.PSet(
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        minTime = cms.double(-3.0),
        stepTwoFromDigi = cms.bool(False),
        doVdriftCorr = cms.bool(True),
        debug = cms.untracked.bool(False),
        tTrigModeConfig = cms.PSet(
            vPropWire = cms.double(24.4),
            doTOFCorrection = cms.bool(True),
            tofCorrType = cms.int32(0),
            wirePropCorrType = cms.int32(0),
            tTrigLabel = cms.string(''),
            doWirePropCorrection = cms.bool(True),
            doT0Correction = cms.bool(True),
            debug = cms.untracked.bool(False)
        ),
        maxTime = cms.double(420.0)
    ),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo')
)

process.DTMeantimerPatternReco2DAlgo_LinearDriftFromDBLoose = cms.PSet(
    Reco2DAlgoConfig = cms.PSet(
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            doVdriftCorr = cms.bool(True),
            debug = cms.untracked.bool(False),
            tTrigModeConfig = cms.PSet(
                vPropWire = cms.double(24.4),
                doTOFCorrection = cms.bool(True),
                tofCorrType = cms.int32(0),
                wirePropCorrType = cms.int32(0),
                tTrigLabel = cms.string(''),
                doWirePropCorrection = cms.bool(True),
                doT0Correction = cms.bool(True),
                debug = cms.untracked.bool(False)
            ),
            maxTime = cms.double(420.0)
        ),
        segmCleanerMode = cms.int32(2),
        perform_delta_rejecting = cms.bool(True),
        MaxT0 = cms.double(100.0),
        performT0_vdriftSegCorrection = cms.bool(False),
        AlphaMaxPhi = cms.double(100.0),
        MaxChi2 = cms.double(4.0),
        hit_afterT0_resolution = cms.double(0.03),
        MaxAllowedHits = cms.uint32(50),
        nSharedHitsMax = cms.int32(2),
        AlphaMaxTheta = cms.double(100.0),
        debug = cms.untracked.bool(False),
        nUnSharedHitsMin = cms.int32(2),
        performT0SegCorrection = cms.bool(False),
        MinT0 = cms.double(-100.0)
    ),
    Reco2DAlgoName = cms.string('DTMeantimerPatternReco')
)

process.DTMeantimerPatternReco4DAlgo_LinearDriftFromDBLoose = cms.PSet(
    Reco4DAlgoName = cms.string('DTMeantimerPatternReco4D'),
    Reco4DAlgoConfig = cms.PSet(
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            doVdriftCorr = cms.bool(True),
            debug = cms.untracked.bool(False),
            tTrigModeConfig = cms.PSet(
                vPropWire = cms.double(24.4),
                doTOFCorrection = cms.bool(True),
                tofCorrType = cms.int32(0),
                wirePropCorrType = cms.int32(0),
                tTrigLabel = cms.string(''),
                doWirePropCorrection = cms.bool(True),
                doT0Correction = cms.bool(True),
                debug = cms.untracked.bool(False)
            ),
            maxTime = cms.double(420.0)
        ),
        Reco2DAlgoConfig = cms.PSet(
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(False),
                doVdriftCorr = cms.bool(True),
                debug = cms.untracked.bool(False),
                tTrigModeConfig = cms.PSet(
                    vPropWire = cms.double(24.4),
                    doTOFCorrection = cms.bool(True),
                    tofCorrType = cms.int32(0),
                    wirePropCorrType = cms.int32(0),
                    tTrigLabel = cms.string(''),
                    doWirePropCorrection = cms.bool(True),
                    doT0Correction = cms.bool(True),
                    debug = cms.untracked.bool(False)
                ),
                maxTime = cms.double(420.0)
            ),
            segmCleanerMode = cms.int32(2),
            perform_delta_rejecting = cms.bool(True),
            MaxT0 = cms.double(100.0),
            performT0_vdriftSegCorrection = cms.bool(False),
            AlphaMaxPhi = cms.double(100.0),
            MaxChi2 = cms.double(4.0),
            hit_afterT0_resolution = cms.double(0.03),
            MaxAllowedHits = cms.uint32(50),
            nSharedHitsMax = cms.int32(2),
            AlphaMaxTheta = cms.double(100.0),
            debug = cms.untracked.bool(False),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            MinT0 = cms.double(-100.0)
        ),
        Reco2DAlgoName = cms.string('DTMeantimerPatternReco'),
        perform_delta_rejecting = cms.bool(True),
        hit_afterT0_resolution = cms.double(0.03),
        performT0_vdriftSegCorrection = cms.bool(False),
        debug = cms.untracked.bool(False),
        nUnSharedHitsMin = cms.int32(2),
        AllDTRecHits = cms.bool(True),
        performT0SegCorrection = cms.bool(False)
    )
)

process.DTTimingExtractorBlock = cms.PSet(
    DTTimingParameters = cms.PSet(
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTsegments = cms.InputTag("dt4DSegments"),
            DTradius = cms.double(0.01),
            TightMatchDT = cms.bool(False),
            TightMatchCSC = cms.bool(True)
        ),
        HitError = cms.double(6.0),
        DoWireCorr = cms.bool(True),
        PruneCut = cms.double(10000.0),
        DTsegments = cms.InputTag("dt4DSegments"),
        DropTheta = cms.bool(True),
        RequireBothProjections = cms.bool(False),
        HitsMin = cms.int32(3),
        DTTimeOffset = cms.double(0.0),
        debug = cms.bool(False),
        UseSegmentT0 = cms.bool(False),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                'PropagatorWithMaterial', 
                'PropagatorWithMaterialOpposite'),
            RPCLayers = cms.bool(True)
        )
    )
)

process.DefaultAlgorithms = cms.PSet(
    CutToAvoidSignal = cms.double(2.0),
    slopeY = cms.int32(4),
    slopeX = cms.int32(3),
    PedestalSubtractionFedMode = cms.bool(False),
    Fraction = cms.double(0.2),
    minStripsToFit = cms.uint32(4),
    consecThreshold = cms.uint32(5),
    hitStripThreshold = cms.uint32(40),
    Deviation = cms.uint32(25),
    CommonModeNoiseSubtractionMode = cms.string('IteratedMedian'),
    filteredBaselineDerivativeSumSquare = cms.double(30),
    ApplyBaselineCleaner = cms.bool(True),
    doAPVRestore = cms.bool(True),
    TruncateInSuppressor = cms.bool(True),
    restoreThreshold = cms.double(0.5),
    APVInspectMode = cms.string('BaselineFollower'),
    ForceNoRestore = cms.bool(False),
    useRealMeanCM = cms.bool(False),
    ApplyBaselineRejection = cms.bool(True),
    DeltaCMThreshold = cms.uint32(20),
    nSigmaNoiseDerTh = cms.uint32(4),
    nSaturatedStrip = cms.uint32(2),
    SiStripFedZeroSuppressionMode = cms.uint32(4),
    useCMMeanMap = cms.bool(False),
    SelfSelectRestoreAlgo = cms.bool(False),
    distortionThreshold = cms.uint32(20),
    filteredBaselineMax = cms.double(6),
    Iterations = cms.int32(3),
    CleaningSequence = cms.uint32(1),
    nSmooth = cms.uint32(9),
    APVRestoreMode = cms.string('BaselineFollower'),
    MeanCM = cms.int32(0)
)

process.DefaultClusterizer = cms.PSet(
    ChannelThreshold = cms.double(2.0),
    MaxSequentialBad = cms.uint32(1),
    Algorithm = cms.string('ThreeThresholdAlgorithm'),
    MaxSequentialHoles = cms.uint32(0),
    MaxAdjacentBad = cms.uint32(0),
    QualityLabel = cms.string(''),
    SeedThreshold = cms.double(3.0),
    RemoveApvShots = cms.bool(True),
    ClusterThreshold = cms.double(5.0)
)

process.GlobalMuonRefitter = cms.PSet(
    TrackerSkipSection = cms.int32(-1),
    MuonHitsOption = cms.int32(1),
    Smoother = cms.string('KFSmootherForRefitInsideOut'),
    RefitDirection = cms.string('insideOut'),
    CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
    Propagator = cms.string('SmartPropagatorAnyRK'),
    TrackerSkipSystem = cms.int32(-1),
    DoPredictionsOnly = cms.bool(False),
    Chi2ProbabilityCut = cms.double(30.0),
    PropDirForCosmics = cms.bool(False),
    HitThreshold = cms.int32(1),
    TrackerRecHitBuilder = cms.string('WithTrackAngle'),
    DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
    Chi2CutCSC = cms.double(1.0),
    Chi2CutRPC = cms.double(1.0),
    Fitter = cms.string('KFFitterForRefitInsideOut'),
    RPCRecSegmentLabel = cms.InputTag("rpcRecHits"),
    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
    DYTthrs = cms.vint32(10, 5),
    RefitRPCHits = cms.bool(True),
    Chi2CutDT = cms.double(30.0),
    PtCut = cms.double(1.0),
    SkipStation = cms.int32(-1)
)

process.GlobalMuonTrackMatcher = cms.PSet(
    GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double(0.0),
        DeltaDCut_3 = cms.double(15.0),
        MinP = cms.double(2.5),
        MinPt = cms.double(1.0),
        Chi2Cut_1 = cms.double(50.0),
        Pt_threshold2 = cms.double(999999999.0),
        LocChi2Cut = cms.double(20.0),
        Eta_threshold = cms.double(1.2),
        Quality_3 = cms.double(7.0),
        Quality_2 = cms.double(15.0),
        Chi2Cut_2 = cms.double(50.0),
        Chi2Cut_3 = cms.double(200.0),
        DeltaDCut_1 = cms.double(2.5),
        DeltaRCut_2 = cms.double(0.2),
        DeltaRCut_3 = cms.double(1.0),
        DeltaDCut_2 = cms.double(10.0),
        DeltaRCut_1 = cms.double(0.1),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        Quality_1 = cms.double(20.0)
    )
)

process.GlobalTrajectoryBuilderCommon = cms.PSet(
    MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double(0.25),
        EtaR_UpperLimit_Par2 = cms.double(0.15),
        OnDemand = cms.double(-1.0),
        Rescale_Dz = cms.double(3.0),
        Eta_min = cms.double(0.1),
        Rescale_phi = cms.double(3.0),
        Eta_fixed = cms.double(0.2),
        DeltaZ_Region = cms.double(15.9),
        MeasurementTrackerName = cms.string(''),
        PhiR_UpperLimit_Par2 = cms.double(0.2),
        vertexCollection = cms.InputTag("pixelVertices"),
        Phi_fixed = cms.double(0.2),
        DeltaR = cms.double(0.2),
        EscapePt = cms.double(1.5),
        UseFixedRegion = cms.bool(False),
        PhiR_UpperLimit_Par1 = cms.double(0.6),
        Rescale_eta = cms.double(3.0),
        Phi_min = cms.double(0.1),
        UseVertex = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    ),
    GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double(0.0),
        DeltaDCut_3 = cms.double(15.0),
        MinP = cms.double(2.5),
        MinPt = cms.double(1.0),
        Chi2Cut_1 = cms.double(50.0),
        Pt_threshold2 = cms.double(999999999.0),
        LocChi2Cut = cms.double(20.0),
        Eta_threshold = cms.double(1.2),
        Quality_3 = cms.double(7.0),
        Quality_2 = cms.double(15.0),
        Chi2Cut_2 = cms.double(50.0),
        Chi2Cut_3 = cms.double(200.0),
        DeltaDCut_1 = cms.double(2.5),
        DeltaRCut_2 = cms.double(0.2),
        DeltaRCut_3 = cms.double(1.0),
        DeltaDCut_2 = cms.double(10.0),
        DeltaRCut_1 = cms.double(0.1),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        Quality_1 = cms.double(20.0)
    ),
    ScaleTECyFactor = cms.double(-1.0),
    GlbRefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32(-1),
        DoPredictionsOnly = cms.bool(False),
        PropDirForCosmics = cms.bool(False),
        HitThreshold = cms.int32(1),
        MuonHitsOption = cms.int32(1),
        Chi2CutRPC = cms.double(1.0),
        Fitter = cms.string('GlbMuKFFitter'),
        DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('insideOut'),
        CSCRecSegmentLabel = cms.InputTag("cscSegments"),
        DYTthrs = cms.vint32(30, 15),
        Chi2CutCSC = cms.double(150.0),
        Chi2CutDT = cms.double(10.0),
        RefitRPCHits = cms.bool(True),
        PtCut = cms.double(1.0),
        Chi2ProbabilityCut = cms.double(30.0),
        SkipStation = cms.int32(-1),
        Propagator = cms.string('SmartPropagatorAnyRK'),
        TrackerSkipSystem = cms.int32(-1)
    ),
    ScaleTECxFactor = cms.double(-1.0),
    TrackerRecHitBuilder = cms.string('WithTrackAngle'),
    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
    RefitRPCHits = cms.bool(True),
    PCut = cms.double(2.5),
    TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True)
    ),
    PtCut = cms.double(1.0),
    TrackerPropagator = cms.string('SteppingHelixPropagatorAny')
)

process.HSCPSelectionDefault = cms.PSet(
    maxMuTimeDtBeta = cms.double(-1),
    onlyConsiderMuonTK = cms.bool(False),
    maxBetaRpc = cms.double(-1),
    onlyConsiderMuonSTA = cms.bool(False),
    onlyConsiderRpc = cms.bool(False),
    minMuTimeDtNdof = cms.double(-1),
    minTrackHits = cms.int32(3),
    minMuTimeCombinedNdof = cms.double(-1),
    onlyConsiderTrack = cms.bool(False),
    minMuonP = cms.double(-1),
    minMTMuonPt = cms.double(-1),
    onlyConsiderMuonGB = cms.bool(False),
    minMuonPt = cms.double(5.0),
    minMuTimeCscNdof = cms.double(-1),
    maxMuTimeCscBeta = cms.double(-1),
    maxBetaEcal = cms.double(-1),
    onlyConsiderMTMuon = cms.bool(False),
    minDedx = cms.double(-1),
    minTrackPt = cms.double(45.0),
    onlyConsiderEcal = cms.bool(False),
    maxMuTimeCombinedBeta = cms.double(-1),
    minSAMuonPt = cms.double(-1),
    minTrackP = cms.double(-1),
    onlyConsiderMuon = cms.bool(False)
)

process.HSCPSelectionEmpty = cms.PSet(
    maxMuTimeDtBeta = cms.double(-1),
    onlyConsiderMuonTK = cms.bool(False),
    maxBetaRpc = cms.double(-1),
    onlyConsiderMuonSTA = cms.bool(False),
    onlyConsiderRpc = cms.bool(False),
    minMuTimeDtNdof = cms.double(-1),
    minTrackHits = cms.int32(-1),
    minMuTimeCombinedNdof = cms.double(-1),
    onlyConsiderTrack = cms.bool(False),
    minMuonP = cms.double(-1),
    minMTMuonPt = cms.double(-1),
    onlyConsiderMuonGB = cms.bool(False),
    minMuonPt = cms.double(-1),
    minMuTimeCscNdof = cms.double(-1),
    maxMuTimeCscBeta = cms.double(-1),
    maxBetaEcal = cms.double(-1),
    onlyConsiderMTMuon = cms.bool(False),
    minDedx = cms.double(-1),
    minTrackPt = cms.double(-1),
    onlyConsiderEcal = cms.bool(False),
    maxMuTimeCombinedBeta = cms.double(-1),
    minSAMuonPt = cms.double(-1),
    minTrackP = cms.double(-1),
    onlyConsiderMuon = cms.bool(False)
)

process.HSCPSelectionHighTOF = cms.PSet(
    maxMuTimeDtBeta = cms.double(0.9),
    onlyConsiderMuonTK = cms.bool(False),
    maxBetaRpc = cms.double(-1),
    onlyConsiderMuonSTA = cms.bool(False),
    onlyConsiderRpc = cms.bool(False),
    minMuTimeDtNdof = cms.double(-1),
    minTrackHits = cms.int32(3),
    minMuTimeCombinedNdof = cms.double(-1),
    onlyConsiderTrack = cms.bool(False),
    minMuonP = cms.double(-1),
    minMTMuonPt = cms.double(-1),
    onlyConsiderMuonGB = cms.bool(False),
    minMuonPt = cms.double(5.0),
    minMuTimeCscNdof = cms.double(-1),
    maxMuTimeCscBeta = cms.double(-1),
    maxBetaEcal = cms.double(-1),
    onlyConsiderMTMuon = cms.bool(False),
    minDedx = cms.double(-1),
    minTrackPt = cms.double(45.0),
    onlyConsiderEcal = cms.bool(False),
    maxMuTimeCombinedBeta = cms.double(-1),
    minSAMuonPt = cms.double(-1),
    minTrackP = cms.double(-1),
    onlyConsiderMuon = cms.bool(True)
)

process.HSCPSelectionHighdEdx = cms.PSet(
    maxMuTimeDtBeta = cms.double(-1),
    onlyConsiderMuonTK = cms.bool(False),
    maxBetaRpc = cms.double(-1),
    onlyConsiderMuonSTA = cms.bool(False),
    onlyConsiderRpc = cms.bool(False),
    minMuTimeDtNdof = cms.double(-1),
    minTrackHits = cms.int32(3),
    minMuTimeCombinedNdof = cms.double(-1),
    onlyConsiderTrack = cms.bool(True),
    minMuonP = cms.double(-1),
    minMTMuonPt = cms.double(-1),
    onlyConsiderMuonGB = cms.bool(False),
    minMuonPt = cms.double(5.0),
    minMuTimeCscNdof = cms.double(-1),
    maxMuTimeCscBeta = cms.double(-1),
    maxBetaEcal = cms.double(-1),
    onlyConsiderMTMuon = cms.bool(False),
    minDedx = cms.double(-1),
    minTrackPt = cms.double(45.0),
    onlyConsiderEcal = cms.bool(False),
    maxMuTimeCombinedBeta = cms.double(-1),
    minSAMuonPt = cms.double(-1),
    minTrackP = cms.double(-1),
    onlyConsiderMuon = cms.bool(False),
    minDedxEstimator1 = cms.double(3.5)
)

process.HSCPSelectionMTMuonOnly = cms.PSet(
    maxMuTimeDtBeta = cms.double(-1),
    onlyConsiderMuonTK = cms.bool(False),
    maxBetaRpc = cms.double(-1),
    onlyConsiderMuonSTA = cms.bool(False),
    onlyConsiderRpc = cms.bool(False),
    minMuTimeDtNdof = cms.double(-1),
    minTrackHits = cms.int32(-1),
    minMuTimeCombinedNdof = cms.double(-1),
    onlyConsiderTrack = cms.bool(False),
    minMuonP = cms.double(-1),
    minMTMuonPt = cms.double(70.0),
    onlyConsiderMuonGB = cms.bool(False),
    minMuonPt = cms.double(-1),
    minMuTimeCscNdof = cms.double(-1),
    maxMuTimeCscBeta = cms.double(-1),
    maxBetaEcal = cms.double(-1),
    onlyConsiderMTMuon = cms.bool(True),
    minDedx = cms.double(-1),
    minTrackPt = cms.double(-1),
    onlyConsiderEcal = cms.bool(False),
    maxMuTimeCombinedBeta = cms.double(-1),
    minSAMuonPt = cms.double(-1),
    minTrackP = cms.double(-1),
    onlyConsiderMuon = cms.bool(False)
)

process.HSCPSelectionSAMuonOnly = cms.PSet(
    maxMuTimeDtBeta = cms.double(-1),
    onlyConsiderMuonTK = cms.bool(False),
    maxBetaRpc = cms.double(-1),
    onlyConsiderMuonSTA = cms.bool(True),
    onlyConsiderRpc = cms.bool(False),
    minMuTimeDtNdof = cms.double(-1),
    minTrackHits = cms.int32(-1),
    minMuTimeCombinedNdof = cms.double(-1),
    onlyConsiderTrack = cms.bool(False),
    minMuonP = cms.double(-1),
    minMTMuonPt = cms.double(-1),
    onlyConsiderMuonGB = cms.bool(False),
    minMuonPt = cms.double(-1),
    minMuTimeCscNdof = cms.double(-1),
    maxMuTimeCscBeta = cms.double(-1),
    maxBetaEcal = cms.double(-1),
    onlyConsiderMTMuon = cms.bool(False),
    minDedx = cms.double(-1),
    minTrackPt = cms.double(-1),
    onlyConsiderEcal = cms.bool(False),
    maxMuTimeCombinedBeta = cms.double(-1),
    minSAMuonPt = cms.double(70.0),
    minTrackP = cms.double(-1),
    onlyConsiderMuon = cms.bool(False)
)

process.MIdIsoExtractorPSetBlock = cms.PSet(
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("generalTracks"),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    ecalDepositName = cms.string('ecal'),
    JetExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(0.5),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("ak5CaloJets"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    ),
    hcalDepositName = cms.string('hcal'),
    CaloExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        Threshold_E = cms.double(0.2),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Threshold_H = cms.double(0.5),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Noise_HO = cms.double(0.2),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            dRHcal = cms.double(1.0),
            dRPreshowerPreselection = cms.double(0.2),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            useEcal = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Noise_HB = cms.double(0.2),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1)
    ),
    trackDepositName = cms.string('tracker'),
    jetDepositName = cms.string('jets'),
    hoDepositName = cms.string('ho')
)

process.MIsoCaloExtractorByAssociatorHitsBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(1.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(1.0),
        useMuon = cms.bool(False),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    ),
    PrintTimeReport = cms.untracked.bool(False),
    DR_Max = cms.double(1.0),
    DepositInstanceLabels = cms.vstring('ecal', 
        'hcal', 
        'ho'),
    Noise_HE = cms.double(0.2),
    NoiseTow_EB = cms.double(0.04),
    NoiseTow_EE = cms.double(0.15),
    Threshold_H = cms.double(0.1),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(False),
        UseMuonNavigation = cms.untracked.bool(False)
    ),
    Noise_HO = cms.double(0.2),
    PropagatorName = cms.string('SteppingHelixPropagatorAny'),
    DepositLabel = cms.untracked.string('Cal'),
    UseRecHitsFlag = cms.bool(True),
    Threshold_HO = cms.double(0.1),
    Noise_EE = cms.double(0.1),
    Noise_EB = cms.double(0.025),
    DR_Veto_H = cms.double(0.1),
    CenterConeOnCalIntersection = cms.bool(False),
    ComponentName = cms.string('CaloExtractorByAssociator'),
    Noise_HB = cms.double(0.2),
    DR_Veto_E = cms.double(0.07),
    DR_Veto_HO = cms.double(0.1),
    Threshold_E = cms.double(0.025)
)

process.MIsoCaloExtractorByAssociatorTowersBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(1.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(False),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(1.0),
        useMuon = cms.bool(False),
        useCalo = cms.bool(True),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(False)
    ),
    PrintTimeReport = cms.untracked.bool(False),
    DR_Max = cms.double(1.0),
    DepositInstanceLabels = cms.vstring('ecal', 
        'hcal', 
        'ho'),
    Noise_HE = cms.double(0.2),
    NoiseTow_EB = cms.double(0.04),
    NoiseTow_EE = cms.double(0.15),
    Threshold_H = cms.double(0.5),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(False),
        UseMuonNavigation = cms.untracked.bool(False)
    ),
    Noise_HO = cms.double(0.2),
    PropagatorName = cms.string('SteppingHelixPropagatorAny'),
    DepositLabel = cms.untracked.string('Cal'),
    UseRecHitsFlag = cms.bool(False),
    Threshold_HO = cms.double(0.5),
    Noise_EE = cms.double(0.1),
    Noise_EB = cms.double(0.025),
    DR_Veto_H = cms.double(0.1),
    CenterConeOnCalIntersection = cms.bool(False),
    ComponentName = cms.string('CaloExtractorByAssociator'),
    Noise_HB = cms.double(0.2),
    DR_Veto_E = cms.double(0.07),
    DR_Veto_HO = cms.double(0.1),
    Threshold_E = cms.double(0.2)
)

process.MIsoCaloExtractorEcalBlock = cms.PSet(
    DR_Veto_H = cms.double(0.1),
    Vertex_Constraint_Z = cms.bool(False),
    Threshold_H = cms.double(0.5),
    ComponentName = cms.string('CaloExtractor'),
    Threshold_E = cms.double(0.2),
    DR_Max = cms.double(1.0),
    DR_Veto_E = cms.double(0.07),
    Weight_E = cms.double(1.0),
    Vertex_Constraint_XY = cms.bool(False),
    DepositLabel = cms.untracked.string('EcalPlusHcal'),
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    Weight_H = cms.double(0.0)
)

process.MIsoCaloExtractorHLTBlock = cms.PSet(
    DR_Veto_H = cms.double(0.1),
    Vertex_Constraint_Z = cms.bool(False),
    Threshold_H = cms.double(0.5),
    ComponentName = cms.string('CaloExtractor'),
    Threshold_E = cms.double(0.2),
    DR_Max = cms.double(1.0),
    DR_Veto_E = cms.double(0.07),
    Weight_E = cms.double(1.5),
    Vertex_Constraint_XY = cms.bool(False),
    DepositLabel = cms.untracked.string('EcalPlusHcal'),
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    Weight_H = cms.double(1.0)
)

process.MIsoCaloExtractorHcalBlock = cms.PSet(
    DR_Veto_H = cms.double(0.1),
    Vertex_Constraint_Z = cms.bool(False),
    Threshold_H = cms.double(0.5),
    ComponentName = cms.string('CaloExtractor'),
    Threshold_E = cms.double(0.2),
    DR_Max = cms.double(1.0),
    DR_Veto_E = cms.double(0.07),
    Weight_E = cms.double(0.0),
    Vertex_Constraint_XY = cms.bool(False),
    DepositLabel = cms.untracked.string('EcalPlusHcal'),
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    Weight_H = cms.double(1.0)
)

process.MIsoDepositGlobalIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("globalMuons"),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('track'),
    InputType = cms.string('TrackCollection')
)

process.MIsoDepositGlobalMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("globalMuons"),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('track'),
    InputType = cms.string('TrackCollection')
)

process.MIsoDepositParamGlobalIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('track'),
    InputType = cms.string('MuonCollection')
)

process.MIsoDepositParamGlobalMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('track'),
    InputType = cms.string('MuonCollection')
)

process.MIsoDepositParamGlobalViewIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('bestTrkSta'),
    InputType = cms.string('MuonCollection')
)

process.MIsoDepositParamGlobalViewMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("paramMuons","ParamGlobalMuons"),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('bestTrkSta'),
    InputType = cms.string('MuonCollection')
)

process.MIsoDepositViewIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("muons1stStep"),
    MultipleDepositsFlag = cms.bool(False),
    MuonTrackRefType = cms.string('bestTrkSta'),
    InputType = cms.string('MuonCollection')
)

process.MIsoDepositViewMultiIOBlock = cms.PSet(
    ExtractForCandidate = cms.bool(False),
    inputMuonCollection = cms.InputTag("muons1stStep"),
    MultipleDepositsFlag = cms.bool(True),
    MuonTrackRefType = cms.string('bestTrkSta'),
    InputType = cms.string('MuonCollection')
)

process.MIsoJetExtractorBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(0.5),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(False),
        dREcal = cms.double(0.5),
        dREcalPreselection = cms.double(0.5),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(False),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.5),
        useMuon = cms.bool(False),
        useCalo = cms.bool(True),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(False)
    ),
    PrintTimeReport = cms.untracked.bool(False),
    ExcludeMuonVeto = cms.bool(True),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(False),
        UseMuonNavigation = cms.untracked.bool(False)
    ),
    ComponentName = cms.string('JetExtractor'),
    DR_Max = cms.double(1.0),
    PropagatorName = cms.string('SteppingHelixPropagatorAny'),
    JetCollectionLabel = cms.InputTag("ak5CaloJets"),
    DR_Veto = cms.double(0.1),
    Threshold = cms.double(5.0)
)

process.MIsoTrackAssociatorDefault = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(1.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(False),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(1.0),
        useMuon = cms.bool(False),
        useCalo = cms.bool(True),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(False)
    )
)

process.MIsoTrackAssociatorHits = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(1.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(1.0),
        useMuon = cms.bool(False),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    )
)

process.MIsoTrackAssociatorJets = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(0.5),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(False),
        dREcal = cms.double(0.5),
        dREcalPreselection = cms.double(0.5),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(False),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.5),
        useMuon = cms.bool(False),
        useCalo = cms.bool(True),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(False)
    )
)

process.MIsoTrackAssociatorTowers = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(1.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(False),
        dREcal = cms.double(1.0),
        dREcalPreselection = cms.double(1.0),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(False),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(1.0),
        useMuon = cms.bool(False),
        useCalo = cms.bool(True),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(False)
    )
)

process.MIsoTrackExtractorBlock = cms.PSet(
    Diff_z = cms.double(0.2),
    inputTrackCollection = cms.InputTag("generalTracks"),
    BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    ComponentName = cms.string('TrackExtractor'),
    DR_Max = cms.double(1.0),
    Diff_r = cms.double(0.1),
    Chi2Prob_Min = cms.double(-1.0),
    DR_Veto = cms.double(0.01),
    NHits_Min = cms.uint32(0),
    Chi2Ndof_Max = cms.double(1e+64),
    Pt_Min = cms.double(-1.0),
    DepositLabel = cms.untracked.string(''),
    BeamlineOption = cms.string('BeamSpotFromEvent')
)

process.MIsoTrackExtractorCtfBlock = cms.PSet(
    Diff_z = cms.double(0.2),
    inputTrackCollection = cms.InputTag("generalTracks"),
    BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    ComponentName = cms.string('TrackExtractor'),
    DR_Max = cms.double(1.0),
    Diff_r = cms.double(0.1),
    Chi2Prob_Min = cms.double(-1.0),
    DR_Veto = cms.double(0.01),
    NHits_Min = cms.uint32(0),
    Chi2Ndof_Max = cms.double(1e+64),
    Pt_Min = cms.double(-1.0),
    DepositLabel = cms.untracked.string(''),
    BeamlineOption = cms.string('BeamSpotFromEvent')
)

process.MIsoTrackExtractorGsBlock = cms.PSet(
    Diff_z = cms.double(0.2),
    inputTrackCollection = cms.InputTag("ctfGSWithMaterialTracks"),
    BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    ComponentName = cms.string('TrackExtractor'),
    DR_Max = cms.double(1.0),
    Diff_r = cms.double(0.1),
    Chi2Prob_Min = cms.double(-1.0),
    DR_Veto = cms.double(0.01),
    NHits_Min = cms.uint32(0),
    Chi2Ndof_Max = cms.double(1e+64),
    Pt_Min = cms.double(-1.0),
    DepositLabel = cms.untracked.string(''),
    BeamlineOption = cms.string('BeamSpotFromEvent')
)

process.MaxConsecLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxConsecLostHitsTrajectoryFilter'),
    maxConsecLostHits = cms.int32(1)
)

process.MaxHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxHitsTrajectoryFilter'),
    maxNumberOfHits = cms.int32(100)
)

process.MaxLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxLostHitsTrajectoryFilter'),
    maxLostHits = cms.int32(1)
)

process.MinHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinHitsTrajectoryFilter'),
    minimumNumberOfHits = cms.int32(5)
)

process.MinPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinPtTrajectoryFilter'),
    nSigmaMinPt = cms.double(5.0),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(1.0)
)

process.MuonCaloCompatibilityBlock = cms.PSet(
    MuonCaloCompatibility = cms.PSet(
        allSiPMHO = cms.bool(False),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    )
)

process.MuonCosmicCompatibilityParameters = cms.PSet(
    CosmicCompFillerParameters = cms.PSet(
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                'SteppingHelixPropagatorAlong', 
                'SteppingHelixPropagatorOpposite', 
                'SteppingHelixPropagatorL2Any', 
                'SteppingHelixPropagatorL2Along', 
                'SteppingHelixPropagatorL2Opposite', 
                'SteppingHelixPropagatorAnyNoError', 
                'SteppingHelixPropagatorAlongNoError', 
                'SteppingHelixPropagatorOppositeNoError', 
                'SteppingHelixPropagatorL2AnyNoError', 
                'SteppingHelixPropagatorL2AlongNoError', 
                'SteppingHelixPropagatorL2OppositeNoError', 
                'PropagatorWithMaterial', 
                'PropagatorWithMaterialOpposite', 
                'SmartPropagator', 
                'SmartPropagatorOpposite', 
                'SmartPropagatorAnyOpposite', 
                'SmartPropagatorAny', 
                'SmartPropagatorRK', 
                'SmartPropagatorAnyRK', 
                'StraightLinePropagator'),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        deltaPt = cms.double(0.1),
        maxdzTight = cms.double(10.0),
        offTimeNegTight = cms.double(-20.0),
        maxvertRho = cms.double(5),
        ipCut = cms.double(0.02),
        segmentComp = cms.double(0.4),
        sharedFrac = cms.double(0.75),
        angleCut = cms.double(0.1),
        hIpTrvProb = cms.double(0.5),
        InputMuonCollections = cms.VInputTag(cms.InputTag("globalMuons"), cms.InputTag("muons1stStep")),
        maxdxyTight = cms.double(1.0),
        maxdzLoose = cms.double(0.1),
        InputTrackCollections = cms.VInputTag(cms.InputTag("generalTracks"), cms.InputTag("cosmicsVetoTracks")),
        maxdxyTightMult = cms.double(1.0),
        corrTimeNeg = cms.double(-10),
        offTimePosTight = cms.double(25.0),
        maxdzLooseMult = cms.double(0.1),
        maxvertZ = cms.double(20),
        nChamberMatches = cms.int32(1),
        corrTimePos = cms.double(5),
        offTimeNegLoose = cms.double(-15.0),
        maxdxyLooseMult = cms.double(0.01),
        offTimePosTightMult = cms.double(25.0),
        offTimePosLoose = cms.double(15.0),
        largedxyMult = cms.double(3.0),
        largedxy = cms.double(2.0),
        nTrackThreshold = cms.int32(3),
        maxdzTightMult = cms.double(10.0),
        InputCosmicMuonCollection = cms.InputTag("muonsFromCosmics1Leg"),
        minvProb = cms.double(0.001),
        hIpTrdxy = cms.double(0.02),
        InputVertexCollection = cms.InputTag("offlinePrimaryVertices"),
        offTimePosLooseMult = cms.double(15.0),
        offTimeNegLooseMult = cms.double(-15.0),
        sharedHits = cms.int32(5),
        maxdxyLoose = cms.double(0.01),
        offTimeNegTightMult = cms.double(-20.0)
    )
)

process.MuonSegmentMatcher = cms.PSet(
    MatchParameters = cms.PSet(
        CSCsegments = cms.InputTag("cscSegments"),
        DTsegments = cms.InputTag("dt4DSegments"),
        DTradius = cms.double(0.01),
        TightMatchDT = cms.bool(False),
        TightMatchCSC = cms.bool(True)
    )
)

process.MuonServiceProxy = cms.PSet(
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'SteppingHelixPropagatorAlong', 
            'SteppingHelixPropagatorOpposite', 
            'SteppingHelixPropagatorL2Any', 
            'SteppingHelixPropagatorL2Along', 
            'SteppingHelixPropagatorL2Opposite', 
            'SteppingHelixPropagatorAnyNoError', 
            'SteppingHelixPropagatorAlongNoError', 
            'SteppingHelixPropagatorOppositeNoError', 
            'SteppingHelixPropagatorL2AnyNoError', 
            'SteppingHelixPropagatorL2AlongNoError', 
            'SteppingHelixPropagatorL2OppositeNoError', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite', 
            'SmartPropagator', 
            'SmartPropagatorOpposite', 
            'SmartPropagatorAnyOpposite', 
            'SmartPropagatorAny', 
            'SmartPropagatorRK', 
            'SmartPropagatorAnyRK', 
            'StraightLinePropagator', 
            'StraightLinePropagator'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    )
)

process.MuonShowerParameters = cms.PSet(
    MuonShowerInformationFillerParameters = cms.PSet(
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                'SteppingHelixPropagatorAlong', 
                'SteppingHelixPropagatorOpposite', 
                'SteppingHelixPropagatorL2Any', 
                'SteppingHelixPropagatorL2Along', 
                'SteppingHelixPropagatorL2Opposite', 
                'SteppingHelixPropagatorAnyNoError', 
                'SteppingHelixPropagatorAlongNoError', 
                'SteppingHelixPropagatorOppositeNoError', 
                'SteppingHelixPropagatorL2AnyNoError', 
                'SteppingHelixPropagatorL2AlongNoError', 
                'SteppingHelixPropagatorL2OppositeNoError', 
                'PropagatorWithMaterial', 
                'PropagatorWithMaterialOpposite', 
                'SmartPropagator', 
                'SmartPropagatorOpposite', 
                'SmartPropagatorAnyOpposite', 
                'SmartPropagatorAny', 
                'SmartPropagatorRK', 
                'SmartPropagatorAnyRK', 
                'StraightLinePropagator'),
            RPCLayers = cms.bool(True),
            UseMuonNavigation = cms.untracked.bool(True)
        ),
        DT4DRecSegmentLabel = cms.InputTag("dt4DSegments"),
        DTRecSegmentLabel = cms.InputTag("dt1DRecHits"),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        CSCSegmentLabel = cms.InputTag("cscSegments"),
        CSCRecSegmentLabel = cms.InputTag("csc2DRecHits"),
        RPCRecSegmentLabel = cms.InputTag("rpcRecHits")
    )
)

process.MuonTrackLoaderForCosmic = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorAny'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        PutTrajectoryIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False),
        AllowNoVertex = cms.untracked.bool(True),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False)
    )
)

process.MuonTrackLoaderForGLB = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(False)
    )
)

process.MuonTrackLoaderForL2 = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("hltOfflineBeamSpot"),
        VertexConstraint = cms.bool(True)
    )
)

process.MuonTrackLoaderForL3 = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(True),
        beamSpot = cms.InputTag("hltOfflineBeamSpot"),
        SmoothTkTrack = cms.untracked.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        Smoother = cms.string('KFSmootherForMuonTrackLoaderL3'),
        VertexConstraint = cms.bool(False),
        DoSmoothing = cms.bool(True)
    )
)

process.MuonTrackLoaderForSTA = cms.PSet(
    TrackLoaderParameters = cms.PSet(
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('SteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        Smoother = cms.string('KFSmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        VertexConstraint = cms.bool(True)
    )
)

process.MuonTrackingRegionCommon = cms.PSet(
    MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double(0.25),
        EtaR_UpperLimit_Par2 = cms.double(0.15),
        OnDemand = cms.double(-1.0),
        Rescale_Dz = cms.double(3.0),
        Eta_min = cms.double(0.1),
        Rescale_phi = cms.double(3.0),
        Eta_fixed = cms.double(0.2),
        DeltaZ_Region = cms.double(15.9),
        MeasurementTrackerName = cms.string(''),
        PhiR_UpperLimit_Par2 = cms.double(0.2),
        vertexCollection = cms.InputTag("pixelVertices"),
        Phi_fixed = cms.double(0.2),
        DeltaR = cms.double(0.2),
        EscapePt = cms.double(1.5),
        UseFixedRegion = cms.bool(False),
        PhiR_UpperLimit_Par1 = cms.double(0.6),
        Rescale_eta = cms.double(3.0),
        Phi_min = cms.double(0.1),
        UseVertex = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot")
    )
)

process.MuonUpdatorAtVertex = cms.PSet(
    MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double(1000000.0),
        Propagator = cms.string('SteppingHelixPropagatorOpposite'),
        BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
    )
)

process.MuonUpdatorAtVertexAnyDirection = cms.PSet(
    MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double(1000000.0),
        Propagator = cms.string('SteppingHelixPropagatorAny'),
        BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
    )
)

process.PixelTripletHLTGenerator = cms.PSet(
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    maxElement = cms.uint32(100000),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    extraHitRPhitolerance = cms.double(0.032),
    useMultScattering = cms.bool(True),
    phiPreFiltering = cms.double(0.3),
    extraHitRZtolerance = cms.double(0.037),
    ComponentName = cms.string('PixelTripletHLTGenerator')
)

process.PixelTripletHLTGeneratorWithFilter = cms.PSet(
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    maxElement = cms.uint32(100000),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
    ),
    extraHitRPhitolerance = cms.double(0.032),
    useMultScattering = cms.bool(True),
    phiPreFiltering = cms.double(0.3),
    extraHitRZtolerance = cms.double(0.037),
    ComponentName = cms.string('PixelTripletHLTGenerator')
)

process.PixelTripletLargeTipGenerator = cms.PSet(
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    maxElement = cms.uint32(100000),
    ComponentName = cms.string('PixelTripletLargeTipGenerator'),
    extraHitRPhitolerance = cms.double(0.0),
    useMultScattering = cms.bool(True),
    phiPreFiltering = cms.double(0.3),
    extraHitRZtolerance = cms.double(0.0)
)

process.RegionPSetBlock = cms.PSet(
    RegionPSet = cms.PSet(
        precise = cms.bool(True),
        originHalfLength = cms.double(21.2),
        originZPos = cms.double(0.0),
        originYPos = cms.double(0.0),
        ptMin = cms.double(0.9),
        originXPos = cms.double(0.0),
        originRadius = cms.double(0.2)
    )
)

process.RegionPSetWithVerticesBlock = cms.PSet(
    RegionPSet = cms.PSet(
        precise = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        useFixedError = cms.bool(True),
        originRadius = cms.double(0.2),
        sigmaZVertex = cms.double(3.0),
        fixedError = cms.double(0.2),
        VertexCollection = cms.InputTag("pixelVertices"),
        ptMin = cms.double(0.9),
        useFoundVertices = cms.bool(True),
        nSigmaZ = cms.double(4.0)
    )
)

process.RegionPsetFomBeamSpotBlock = cms.PSet(
    RegionPSet = cms.PSet(
        precise = cms.bool(True),
        nSigmaZ = cms.double(4.0),
        originRadius = cms.double(0.2),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        ptMin = cms.double(0.9)
    )
)

process.SiPixelGainCalibrationServiceParameters = cms.PSet(

)

process.TECi = cms.PSet(
    minRing = cms.int32(1),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    useRingSlector = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    maxRing = cms.int32(2)
)

process.ThresholdPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ThresholdPtTrajectoryFilter'),
    nSigmaThresholdPt = cms.double(5.0),
    minHitsThresholdPt = cms.int32(3),
    thresholdPt = cms.double(10.0)
)

process.TimingFillerBlock = cms.PSet(
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            HitError = cms.double(6.0),
            DoWireCorr = cms.bool(True),
            PruneCut = cms.double(10000.0),
            DTsegments = cms.InputTag("dt4DSegments"),
            DropTheta = cms.bool(True),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(3),
            DTTimeOffset = cms.double(0.0),
            debug = cms.bool(False),
            UseSegmentT0 = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            )
        ),
        CSCTimingParameters = cms.PSet(
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("cscSegments"),
                DTsegments = cms.InputTag("dt4DSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            CSCsegments = cms.InputTag("csc2DSegments"),
            CSCStripTimeOffset = cms.double(0.0),
            CSCStripError = cms.double(7.0),
            UseStripTime = cms.bool(True),
            debug = cms.bool(False),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(9.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(True)
    )
)

process.TrackAssociatorParameterBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    )
)

process.TrackAssociatorParameters = cms.PSet(
    muonMaxDistanceSigmaX = cms.double(0.0),
    muonMaxDistanceSigmaY = cms.double(0.0),
    CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
    dRHcal = cms.double(9999.0),
    dREcal = cms.double(9999.0),
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    useEcal = cms.bool(True),
    dREcalPreselection = cms.double(0.05),
    HORecHitCollectionLabel = cms.InputTag("horeco"),
    dRMuon = cms.double(9999.0),
    propagateAllDirections = cms.bool(True),
    muonMaxDistanceX = cms.double(5.0),
    muonMaxDistanceY = cms.double(5.0),
    useHO = cms.bool(True),
    trajectoryUncertaintyTolerance = cms.double(-1.0),
    usePreshower = cms.bool(False),
    DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
    EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    dRHcalPreselection = cms.double(0.2),
    useMuon = cms.bool(True),
    useCalo = cms.bool(False),
    accountForTrajectoryChangeCalo = cms.bool(False),
    EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    dRMuonPreselection = cms.double(0.2),
    truthMatch = cms.bool(False),
    HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
    useHcal = cms.bool(True)
)

process.TrackerKinkFinderParametersBlock = cms.PSet(
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        usePosition = cms.bool(True),
        diagonalOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite')
    )
)

process.dphiScale = cms.PSet(
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0)
)

process.fieldScaling = cms.PSet(
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991)
)

process.layerInfo = cms.PSet(
    TEC4 = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        maxRing = cms.int32(2)
    ),
    TEC5 = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        maxRing = cms.int32(2)
    ),
    TEC6 = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        maxRing = cms.int32(2)
    ),
    TEC = cms.PSet(
        minRing = cms.int32(5),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(False),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        maxRing = cms.int32(7)
    ),
    TEC1 = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        maxRing = cms.int32(2)
    ),
    TEC2 = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        maxRing = cms.int32(2)
    ),
    TEC3 = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        maxRing = cms.int32(2)
    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TID = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(False),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.ptSeedParameterization = cms.PSet(
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, -0.0, 0.067, -0.001, 
        0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0)
)

process.schedule = cms.Schedule(*[ process.pPF ])

