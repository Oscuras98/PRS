from flask import Flask
from flask import render_template

app = Flask(__name__)

#   Main Menu
# 1  Home
@app.route('/')
def home():
    return render_template('ENG/1_Home/1_home_ENG.html');
# 1 Inicio
@app.route('/inicio')
def inicio():
    return render_template('ESP/1_Inicio/1_inicio_ESP.html');
# 1 Kezdolap
@app.route('/index')
def index():
    return render_template('HUN/1_Index/1_index_HUN.html');

# Main Menu Drop Button 2
# 2 Learn To Code
@app.route('/Learn_ENG')
def Learn_ENG():
	return render_template('ENG/2_Learn/Learn_ENG.html');
# 2 Aprende Programar
@app.route('/Aprender_ESP')
def Aprender_ESP():
	return render_template('ESP/2_Aprender/Aprender_ESP.html');
# 2 Tanulj Programozni
@app.route('/Programozni_HUN')
def Programozni_HUN():
	return render_template('HUN/2_Programozni_HUN/Programozni_HUN.html');

	# Learn C++ Sub Menu
	# Estudia C++ Sub menu
	# Tanulj C++ -t Sub Menu
@app.route('/CPP_1_ENG')
def CPP_1_ENG():
	return render_template('ENG/2_Learn/CPP_ENG/CPP_1_ENG.html');
@app.route('/CPP_1_ESP')
def CPP_1_ESP():
	return render_template('ESP/2_Aprender/CPP_ESP/CPP_1_ESP.html');
@app.route('/CPP_1_HUN')
def CPP_1_HUN():
	return render_template('HUN/2_Programozni_HUN/CPP_HUN/CPP_1_HUN.html');
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
@app.route('/CPP_2_ENG')
def CPP_2_ENG():
	return render_template('ENG/2_Learn/CPP_ENG/CPP_2_ENG.html');
@app.route('/CPP_2_ESP')
def CPP_2_ESP():
	return render_template('ESP/2_Aprender/CPP_ESP/CPP_2_ESP.html'); 
@app.route('/CPP_2_HUN')
def CPP_2_HUN():
	return render_template('HUN/2_Programozni_HUN/CPP_HUN/CPP_2_HUN.html');
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
@app.route('/CPP_3_ENG')
def CPP_3_ENG():
	return render_template('ENG/2_Learn/CPP_ENG/CPP_3_ENG.html');
@app.route('/CPP_3_ESP')
def CPP_3_ESP():
	return render_template('ESP/2_Aprender/CPP_ESP/CPP_3_ESP.html'); 
@app.route('/CPP_3_HUN')
def CPP_3_HUN():
	return render_template('HUN/2_Programozni_HUN/CPP_HUN/CPP_3_HUN.html');
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
@app.route('/CPP_4_ENG')
def CPP_4_ENG():
	return render_template('ENG/2_Learn/CPP_ENG/CPP_4_ENG.html');
@app.route('/CPP_4_ESP')
def CPP_4_ESP():
	return render_template('ESP/2_Aprender/CPP_ESP/CPP_4_ESP.html'); 
@app.route('/CPP_4_HUN')
def CPP_4_HUN():
	return render_template('HUN/2_Programozni_HUN/CPP_HUN/CPP_4_HUN.html');
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Main Menu Drop Button 3
# 3 Pentest
@app.route('/Pentest_1_ENG')
def Pentest_1_ENG():
	return render_template('ENG/3_Pentest/Pentest_1_ENG.html');
# 3 Penetracion
@app.route('/Penetracion_1_ESP')
def Penetracion_1_ESP():
	return render_template('ESP/3_Penetracion/Penetracion_1_ESP.html');
# 3 Penteszt
@app.route('/Penteszt_1_HUN')
def Penteszt_1_HUN():
	return render_template('HUN/3_Penteszt/Penteszt_1_HUN.html');


# 4 Free Games
@app.route('/Free_GAMES_ENG')
def Free_GAMES_ENG():
	return render_template('ENG/4_Free_Games/Free_GAMES_ENG.html');
# 4 Juegos Gratis
@app.route('/Juegos_GRATIS_ESP')
def Juegos_GRATIS_ESP():
	return render_template('ESP/4_Juegos_Gratis/Juegos_GRATIS_ESP.html');
# 4 Ingyenes Jatekok
@app.route('/Free_JATEKOK_HUN')
def Free_JATEKOK_HUN():
	return render_template('HUN/4_Free_Jatekok/Free_JATEKOK_HUN.html');



# 5 DONATIONS
@app.route('/Donations_ENG')
def Donations_ENG():
	return render_template('ENG/5_Donate/Donate_ENG.html');
# 5 DONACIONES
@app.route('/Donaciones_ESP')
def Donaciones_ESP():
	return render_template('ESP/5_Donaciones/Donaciones_ESP.html');
# 5 SPONZORALAS
@app.route('/Sponzor_HUN')
def Sponzor_HUN():
	return render_template('HUN/5_Sponzor/Sponzor_HUN.html');


# WORLD OF TANKS SPAIN
@app.route('/WOT_SPAIN')
def WOT_SPAIN():
	return render_template('ESP/6_World_Of_Tanks_Spain/WOT_SPAIN.html');

if __name__ == '__main__':
    app.run()
