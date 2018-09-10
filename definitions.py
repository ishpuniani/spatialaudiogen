AUDIO = 'audio'
VIDEO = 'video'
FLOW = 'flow'
ENCODERS = [AUDIO, VIDEO, FLOW]

NO_SEPARATION = 'none'
FREQ_MASK = 'unet_mask'
SEPARATION = [NO_SEPARATION, FREQ_MASK]

FFT_WINDOW = 25 * 0.001  # sec
FFT_OVERLAP_R = 2  # number of window overlaps

NUM_SEP_TRACKS_DEF = 32
CTX_FEATS_FCUNITS_DEF = [64, 128, 128]
SEP_FREQ_MASK_FCUNITS_DEF = [256]
LOC_FCUNITS_DEF = [512, 512]
SEP_FFT_WINDOW_DEF = 0.025