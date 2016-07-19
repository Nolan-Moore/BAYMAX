import em
em.eulerian_magnification('/home/pi/BAYMAX/Results/practice.mp4',
                          image_processing='gaussian',
                          pyramid_levels=3,
                          freq_min = 50.0/60.0,
                          freq_max = 1.7,
                          amplification = 40)
#em.show_frequencies('/home/pi/BAYMAX/Results/face.mp4')
#em.show_frequencies('/home/pi/BAYMAX/Results/resultVideo_magnified.avi')
em.get_pulse('/home/pi/BAYMAX/Results/resultVideo_magnified.avi')
