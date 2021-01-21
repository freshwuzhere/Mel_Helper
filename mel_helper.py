import ui
import datetime
import time
from dialogs import list_dialog
from math import floor
import speech

# Add Globals
start_time = datetime.datetime.now() + datetime.timedelta(hours=1)
port_entry = "INEOS"
stbd_entry = "LUNA ROSSA"
start_time_pick = start_time
v = None
sound_set = True
possible_boats = ['INEOS','LUNA ROSSA','AM MAGIC','ETNZ']
old_stg = 0
old_mtg = 0
old_stg_x10 = 0

def pick_start_time(sender):
	global start_time_pick
	global v
	print('in timer loop')
	s_t_p = v['start_time_picker']
	
	start_time_pick_hm  = s_t_p.date
	start_time_pick = start_time_pick_hm.replace(second=0)
	
	print(str(start_time_pick))
	
	#change color so you know it's not set
	s_t_p.background_color = 'red'
	
	print(str(start_time_pick))
	#speech.say(str(t_time))
	
def pick_port_entry(sender):
	global v
	global possible_boats
	# make a list - add selection
	
	selected_boats_list = list_dialog(title = 'Select the Boats',items = possible_boats,multiple = False)
	
	p_b_ui = v['port_boat']
	
	p_b_ui.text = selected_boats_list
		
		
def pick_stbd_entry(sender):
	global v
	global possible_boats
	# make a list - add selection
	
	selected_boats_list = list_dialog(title = 'Select the Boats',items = possible_boats,multiple = False)
	
	p_b_ui = v['stbd_boat']
	p_b_ui.text = selected_boats_list
	
def set_sound(sender):
	global v
	global sound_set
	
	ss = v['sound_switch']
	sound_set = ss.value
	# speech.say('sound set ' + str(ss.value))
	
def set_start_time(sender):
	global start_time
	global start_time_pick
	global v
	
	start_time = start_time_pick
	s_t_p = v['start_time_picker']
	
	#change color so you know it's not set
	s_t_p.background_color = 'white'
	
def set_count_down(st_time, htg_lab , mtg_lab , stg_lab, dtg_lab):
	global start_time
	global old_mtg
	global old_stg
	global old_stg_x10
	global sound_set
	
	NOW = datetime.datetime.now()
	if start_time >= NOW :
		delta = (start_time - NOW)
		count_down = True
	else:
		delta = (NOW - start_time )
		count_down = False
		
	secs = delta.total_seconds()
	
	htg = secs // 3600
	htg_s = '{:02.0f}'.format(htg)
	
	mtg = (secs - (htg * 3600)) // 60
	mtg_s = '{:02.0f}'.format(mtg)
	
	stg = secs - ( htg * 3600 ) - (mtg * 60 )
	stg_s = '{:02.0f}'.format(stg)
	
	stg_x10 =  stg//10 * 10 #should be round 10 sec steps
		
	dtg = floor((secs - secs//1)*10)
	dtg_s = '{:.0f}'.format(dtg)
	
#	print('formatted time' + htg_s + ':' +  mtg_s + ':' + stg_s + '.' + dtg_s)	
#	print('secs = ' + str(secs) + 'trunc secs' + str(secs//1) )

#	test for speech - start with seconds		
	htg_r = floor(htg)
	mtg_r = floor(mtg)
	stg_r = floor(stg)
	#print('old = ' + str(old_stg) + 'stg_r = ' + str(stg_r))
	if sound_set:
		if old_mtg != mtg_r and count_down:
			speech.say('{:.0f}'.format(mtg_r + 1) + ' minutes')
		elif stg_x10 != old_stg_x10:
			if mtg_r == 0 and htg_r == 0 and count_down:
				speech.say('{:.0f} seconds'.format(stg_x10+10))
		elif  old_stg != stg_r:
			if stg <= 10 and count_down and mtg_r == 0 and htg_r == 0  :
				speech.say('{:.0f}'.format(stg_r + 1))
	if round(stg,1) == 0 and mtg_r == 0  and htg_r ==0 :
		speech.say("START")
				
					
			
	old_mtg = mtg_r
	old_stg = stg_r
	old_stg_x10 = stg_x10
	
	htg_lab.text = htg_s
	mtg_lab.text = mtg_s
	stg_lab.text = stg_s
	dtg_lab.text = dtg_s

def will_close(self):
	self.close
	return 
		
def main():
	global v
	global start_time

	v = ui.load_view()

	start_time_ui_val = v['start_time_picker']
	start_time_ui_val.date = start_time
	
	v.present('sheet')
	
	print('Start Time = ' + str(start_time))
	h_t_g = v['hours_to_go']
	m_t_g = v['mins_to_go']
	s_t_g = v['secs_to_go']
	d_t_g = v['decimals_to_go']

	while True:
		set_count_down(start_time,
										h_t_g, 
										m_t_g,
										s_t_g,
										d_t_g)
		time.sleep(0.1)

if __name__ == '__main__':
	main()
	sys.exit()

