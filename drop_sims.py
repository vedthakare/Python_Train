from make_sims import make_sim

source_dir = r"C:\Users\ved.thakare\OneDrive - University of Virginia\vanilla_blower"
main_dir = r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights"

Parameters = {'vent': [3.0],
              'start': [1000],
              'height': [12,24,30],
              'blow_v': [14000], # got rid of 5000
              'blow_s': [300],
              'stiffness': [0.1,0.3,0.5]}

for i in Parameters['vent']:
    for j in Parameters['start']:
        for k in Parameters['height']:
            for l in Parameters['blow_v']:
                for m in Parameters['blow_s']:
                    for n in Parameters['stiffness']:
                        parameters = {'vent_d': i,
                                      'start': j,
                                      'term': 2000,
                                      'height': k,
                                      'blow_v': l,
                                      'blow_s': m,
                                      'ea': n}

                        make_sim(parameters, source_dir, main_dir)
