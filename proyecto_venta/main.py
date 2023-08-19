import sys

clients = 'carlos,pedro,'

''' 
clients += client_name
UnboundLocalError: local variable 'clients' referenced before assignment

La solución es agregar el keyword 'global' clients
 '''

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)

def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')

    else: 
        print('Client is not in the clients list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')

    else: 
        print('Client is not in the clients list')

def search_client(client_name):
    client_list = clients.split(',')

    for client in client_list:
        if client != client_name:
            continue
        else:
            return True


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('WELCOME TO TIENDA VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


# PUNTO DE ENTRADA
if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
        pass
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list.')
        else:
            # {} = placeholder
            print('The client: {} is not in our client\'s list.'.format(client_name))

    else:
        print('Invalid command')