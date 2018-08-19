from flask import Flask, request, render_template, redirect, Markup, flash
from MC_Contract import Contract
from MC_Contract import contracts as bets
from flask_table import Table, Col 
import grpc
import pickle
import send_info_pb2
import send_info_pb2_grpc
import socket 

_APP_IP = socket.gethostbyname(socket.gethostname())
_APP_PORT = 12345 # port used in full_node 


# pass it in to help out flask
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        pass

    # connect to the main program and see what contracts currently exist
    real_bets = []

    '''
    with grpc.insecure_channel(f'{_APP_IP}:{_APP_PORT}') as channel:
        stub = send_info_pb2_grpc.SendInfoStub(channel)
        response = stub.ContractDisplay(send_info_pb2.ContractRequest(
                                                message = 'SEND ME ALL THE BETS'))

    if len(response.contracts) == 0:
        return 'There are no bets to be found!'
    else:
        for contract in response.contracts:
            real_bets.append(pickle.loads(contract))
    '''
    return render_template('bets.html',bets=bets) #change back to real_bets after implementing GRPC

@app.route('/accept_bet/<string:bet_id>',methods=['GET','POST'])
def accept_bet(bet_id):
    # send the transaction hash to the main program 
    '''
    with grpc.insecure_channel(f'{_APP_IP}:{_APP_PORT}') as channel:
        stub = send_info_pb2_grpc.SendInfoStub(channel)
        response = stub.TransactionCreation(send_info_pb2.TransactionRequest(
                                            txn_hash = bet_id))
    if response.message == '200 OK':
        print ('success')
    else:
        print ('failure')
    '''

    return redirect('/')

@app.route('/create_contract')
def create_contract():
    return render_template('create.html')

# this method is for when the user wants to create a contract
@app.route('/post_contract',methods=['POST'])
def post_contract():
    event = request.form['event']
    team = request.form['team']
    quantity = request.form['quantity']
    expiration_date = request.form['expiration_date']
    odds = request.form['odds']
    source_of_truth = request.form['source_of_truth']
    check_result_time = request.form['check_result_time']
    party1_public_key = request.form['party1_public_key']
    party1_digital_sig = request.form['party1_digital_sig']
    print ('--------------------------------------------------------------')
    print (event,team,quantity,expiration_date,odds,source_of_truth,
                    check_result_time,party1_public_key,party1_digital_sig)
    print ('--------------------------------------------------------------')
    '''
    with grpc.insecure_channel(f'{_APP_IP}:{_APP_PORT}') as channel:
        stub = send_info_pb2_grpc.SendInfoStub(channel)

        the_contract = Contract(event,team,quantity,expiration_date,odds,source_of_truth,
                                check_result_time,party1_public_key,party1_digital_sig)
        response = stub.ContractCreation(send_info_pb2.ContractCreationRequest(
                                            contract = pickle.dumps(the_contract)))
    if response.message == '200 OK':
        print ('success')
    else:
        print ('failure')
    '''

    return redirect('/')

if __name__ == '__main__':
    #app.secret_key = 'super secret key'
    #app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)
    app.run(debug=True) # when we're in developer mode 




























