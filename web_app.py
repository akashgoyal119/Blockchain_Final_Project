from flask import Flask, request, render_template, redirect, Markup, flash
from MagicCoin.MC_Contract import Contract
import grpc
import pickle
#import send_info_pb2
#import send_info_pb2_grpc
import full_node_pb2
import full_node_pb2_grpc 
import socket 
import time
import datetime

_APP_IP = socket.gethostbyname(socket.gethostname())
_APP_PORT = 12345 # port used in full_node 


# pass it in to help out flask
app = Flask(__name__)

@app.template_filter('strftime')
def _jinja2_filter_datetime(date):
    return datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        pass

    # connect to the main program and see what contracts currently exist
    real_bets = []

    with grpc.insecure_channel(f'{_APP_IP}:{_APP_PORT}') as channel:
        stub = full_node_pb2_grpc.FullNodeStub(channel)
        the_request = full_node_pb2.ExistingContractRequest(message= '___')
        response = stub.show_all_existing_contracts(the_request)

    if len(response.serialized_contracts) == 0:
        print ('There are no bets to be found!')
    else:
        for contract in response.serialized_contracts:
            real_bets.append(pickle.loads(contract))

    print ('success?')

    return render_template('bets.html',bets=real_bets) #change back to real_bets after implementing GRPC

@app.route('/txn_detail/<txn>')
def get_transaction_details(txn):
    transaction = txn
    return render_template('transaction_detail.html',txn=transaction)

@app.route('/accept_bet/<string:bet_id>',methods=['GET','POST'])
def accept_bet(bet_id):
    # send the transaction hash to the main program 
    '''
    with grpc.insecure_channel(f'{_APP_IP}:{_APP_PORT}') as channel:
        stub = send_info_pb2_grpc.SendInfoStub(channel)
        response = stub.TransactionCreation(send_info_pb2.TransactionRequest(
                                            txn_hash = bet_id))
    '''

    return redirect('/')

@app.route('/create_contract')
def create_contract():
    return render_template('create.html')


@app.route('/blockchain')
def get_blockchain():

    with grpc.insecure_channel(f'{_APP_IP}:{_APP_PORT}') as channel:
        stub = full_node_pb2_grpc.FullNodeStub(channel)
        the_request = full_node_pb2.BlockchainRequest(message= '___')
        response = stub.display_full_blockchain(the_request)

    bc = pickle.loads(response.response)
    return render_template('blockchain.html',bc=bc)


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

    expiration_date = time.mktime(datetime.datetime.strptime(expiration_date,'%Y-%m-%dT%H:%M').timetuple())
    check_result_time = time.mktime(datetime.datetime.strptime(check_result_time,'%Y-%m-%dT%H:%M').timetuple())

    the_contract = Contract(event,team,quantity,expiration_date,odds,source_of_truth,
                                check_result_time,party1_public_key,party1_digital_sig)
    print (the_contract)
    
    with grpc.insecure_channel(f'{_APP_IP}:{_APP_PORT}') as channel:
        #stub = send_info_pb2_grpc.SendInfoStub(channel)
        stub = full_node_pb2_grpc.FullNodeStub(channel)
        

        contract = full_node_pb2.Contract(serialized_contract=pickle.dumps(the_contract),
                                          broadcast_node=_APP_IP)
        stub.new_contract_broadcast(contract)

    print ('made it successfully?')
    return redirect('/')

if __name__ == '__main__':
    #app.secret_key = 'super secret key'
    #app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)
    app.run(debug=True,host='0.0.0.0') # when we're in developer mode 




























