from flask import Flask, render_template, request ,redirect, session
from datetime import datetime
import random 	

app = Flask(__name__)
app.secret_key = 'clavesecreta' # asignar una clave secreta por motivos de seguridad

@app.route('/')
def begin_game():
    if 'gold' not in session:  #si no se hay variable de sesión se crea una
        session['gold'] = 0
        session['activities'] = "¡ Begin the Game !" + "\n"
        session['activities'] = ""
        print(f"Inicio de Juego!!------{session['gold']} --------------")
      

    if session['gold'] < 0: #si el oro es menor que 0 se ha acabado el juego y se esconden los forms para evitar seguir jugando
        
        session['activities'] += (f"<div class='gameover'> You lose -------------GAME OVER------------- </div>")
        return render_template('/index.html' , unhide_playagain = "yes", unhide_reset = "none")

    return render_template('/index.html' , unhide_playagain = "none", unhide_reset = "yes") # si existe sesión y el oro es mayor o igual a 0 se sigue jugando

@app.route('/process_money', methods = ['POST'])
def process_money():
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")  
    
    if request.form['site'] == "farm": # se se va a la granja
        print("farm")
        numero =  random.randint(10, 20) #probabilidad de ganar oro
        session['gold'] += numero
        session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the Farm! ({str(time)})</div>")

    if request.form['site'] == "cave": # se se va a la cueva
        print("cave") 
        numero =  random.randint(5, 10)  #probabilidad de ganar oro
        session['gold'] += numero 
        session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the Cave! ({str(time)})</div>")

    if request.form['site'] == "house": # se se va a la casa
        print("house") 
        numero =  random.randint(2, 5) #probabilidad de ganar oro
        session['gold'] += numero
        session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the House! ({str(time)})</div>")

    if request.form['site'] == "casino": # se se va al casino
        print("casino")  
        numero =  random.randint(-50, 50) #probabilidad de ganar o perder oro
        session['gold'] += numero
        if numero<0: #si pierde oro
            session['activities'] += (f"<div class='red'>Entered a casino and lost {str(numero)} golds... Ouch..  ({str(time)})</div>")
        else: #si gana oro
            session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the Casino! ({str(time)})</div>")

    print(request.form)
    print("*"*20)
  
    return redirect('/')

@app.route('/reset') #elimina las variables de sesión
def reset():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)