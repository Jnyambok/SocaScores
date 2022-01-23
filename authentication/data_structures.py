import pandas as pd
import pickle
import os
os.chdir(r"C:\Users\hp\Downloads")



class stats():
    team_name=['Manchester City','Chelsea','Liverpool','West Ham United','Arsenal','Tottenham Hotspur','Manchester United','Brighton and Hove Albion','WolverHampton Wanderers',
    'Leicester','Southampton','Crystal Palace','Brentford','Aston Villa','Everton','Leeds','Watford','Burnley','Newcastle United','Norwich']


    standard_stats=['https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb8fd03ef%2FManchester-City-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcff3d9bb%2FChelsea-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F822bd0ba%2FLiverpool-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F7c21e445%2FWest-Ham-United-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F18bb7c10%2FArsenal-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F361ca564%2FTottenham-Hotspur-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F19538871%2FManchester-United-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd07537b9%2FBrighton-and-Hove-Albion-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8cec06e1%2FWolverhampton-Wanderers-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fa2d435b3%2FLeicester-City-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F33c895d4%2FSouthampton-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F47c64c55%2FCrystal-Palace-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcd051869%2FBrentford-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8602292d%2FAston-Villa-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd3fd31cc%2FEverton-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F5bfb9659%2FLeeds-United-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F2abfe087%2FWatford-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F943e8050%2FBurnley-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb2b47a98%2FNewcastle-United-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F1c781004%2FNorwich-City-Stats&div=div_stats_standard_11160&del_col=4,11,12,13,24,27,28,29,30'
    ]



    scores_=['https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb8fd03ef%2FManchester-City-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcff3d9bb%2FChelsea-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F822bd0ba%2FLiverpool-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F7c21e445%2FWest-Ham-United-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F18bb7c10%2FArsenal-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F361ca564%2FTottenham-Hotspur-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F19538871%2FManchester-United-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd07537b9%2FBrighton-and-Hove-Albion-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8cec06e1%2FWolverhampton-Wanderers-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fa2d435b3%2FLeicester-City-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F33c895d4%2FSouthampton-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F47c64c55%2FCrystal-Palace-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcd051869%2FBrentford-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8602292d%2FAston-Villa-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd3fd31cc%2FEverton-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F5bfb9659%2FLeeds-United-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F2abfe087%2FWatford-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F943e8050%2FBurnley-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb2b47a98%2FNewcastle-United-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F1c781004%2FNorwich-City-Stats&div=div_matchlogs_for&del_col=5,14,15,17,18,19']





    shooting_=['https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb8fd03ef%2FManchester-City-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcff3d9bb%2FChelsea-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F822bd0ba%2FLiverpool-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F7c21e445%2FWest-Ham-United-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F18bb7c10%2FArsenal-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F361ca564%2FTottenham-Hotspur-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F19538871%2FManchester-United-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd07537b9%2FBrighton-and-Hove-Albion-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8cec06e1%2FWolverhampton-Wanderers-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fa2d435b3%2FLeicester-City-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F33c895d4%2FSouthampton-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F47c64c55%2FCrystal-Palace-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcd051869%2FBrentford-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8602292d%2FAston-Villa-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd3fd31cc%2FEverton-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F5bfb9659%2FLeeds-United-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F2abfe087%2FWatford-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F943e8050%2FBurnley-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb2b47a98%2FNewcastle-United-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F1c781004%2FNorwich-City-Stats&div=div_stats_shooting_11160&del_col=13,14,15,16,17,20,21,22,23'

    ]




    playing_=['https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb8fd03ef%2FManchester-City-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcff3d9bb%2FChelsea-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F822bd0ba%2FLiverpool-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F7c21e445%2FWest-Ham-United-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F18bb7c10%2FArsenal-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F361ca564%2FTottenham-Hotspur-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F19538871%2FManchester-United-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd07537b9%2FBrighton-and-Hove-Albion-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8cec06e1%2FWolverhampton-Wanderers-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fa2d435b3%2FLeicester-City-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F33c895d4%2FSouthampton-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F47c64c55%2FCrystal-Palace-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fcd051869%2FBrentford-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F8602292d%2FAston-Villa-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fd3fd31cc%2FEverton-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F5bfb9659%2FLeeds-United-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F2abfe087%2FWatford-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F943e8050%2FBurnley-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2Fb2b47a98%2FNewcastle-United-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27',
    'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fsquads%2F1c781004%2FNorwich-City-Stats&div=div_stats_playing_time_11160&del_col=4,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27'
    ]

    team= 'Brighton and Hove Albion'
    df=pd.DataFrame({'StandardStats':standard_stats,'Res_Fixtures':scores_,'Shoot_stats':shooting_,'Playing_time':playing_},index=team_name)
    #print(df)


    for index,rows in df.iterrows():
        if team == index:
            i=(rows[0])
    print(i)

