import ui
import datetime
import time
from dialogs import list_dialog
from math import floor
#import speech

# Add Globals
start_time = datetime.datetime.now() + datetime.timedelta(hours=1)
port_entry = "OTUSA"
stbd_entry = "ARTEMIS"
start_time_pick = start_time
v = None
possible_boats = ['OTUSA','SBTJ','ARTEMIS','LRBAR','GROUPAMA','ETNZ']

def pick_start_time(sender):
	global start_time_pick
	global v
	print('in timer loop')
	s_t_p = v['start_time_picker']
	
	start_time_pick  = s_t_p.date
	
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
	
	
#	if p_b_ui.text == 'OTUSA':
#		p_b_ui.text = 'SBTJ'
#	else:
#		p_b_ui.text = 'OTUSA'	
		
def pick_stbd_entry(sender):
	global v
	global possible_boats
	# make a list - add selection
	
	selected_boats_list = list_dialog(title = 'Select the Boats',items = possible_boats,multiple = False)
	
	p_b_ui = v['stbd_boat']
	
	p_b_ui.text = selected_boats_list
	
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
	
	delta = (start_time - datetime.datetime.now())
	secs = delta.total_seconds()
	
	htg = secs // 3600
	htg_s = '{:02.0f}'.format(htg)
	
	mtg = (secs - (htg * 3600)) // 60
	mtg_s = '{:02.0f}'.format(mtg)
	
	stg = secs - ( htg * 3600 ) - (mtg * 60 )
	stg_s = '{:02.0f}'.format(stg)
	
	dtg = floor((secs - secs//1)*10)
	dtg_s = '{:.0f}'.format(dtg)
	
#	print('formatted time' + htg_s + ':' +  mtg_s + ':' + stg_s + '.' + dtg_s)	
#	print('secs = ' + str(secs) + 'trunc secs' + str(secs//1) )
	
	htg_lab.text = htg_s
	mtg_lab.text = mtg_s
	stg_lab.text = stg_s
	dtg_lab.text = dtg_s
	
def main():
	global v
	v = ui.load_view()
	v.present('sheet')

	global start_time

	print('Start Time = ' + str(start_time))
	h_t_g = v['hours_to_go']
	m_t_g = v['mins_to_go']
	s_t_g = v['secs_to_go']
	d_t_g = v['decimals_to_go']

	start_time_ui_val = v['start_time_picker']

	while True:
		set_count_down(start_time,
										h_t_g, 
										m_t_g,
										s_t_g,
										d_t_g)
		time.sleep(0.1)

if __name__ == '__main__':
	main()

