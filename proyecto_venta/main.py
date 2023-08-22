import sys

# clients = ['carlos','pedro,']
clients = [
    {
        'name': 'Carlos',
        'company': 'Google',
        'email': 'carlos@google.com',
        'position': 'Data Enginner'
    },
    {
        'name': 'Pedro',
        'company': 'Google',
        'email': 'pedro@google.com',
        'position': 'Software Enginner'
    }
]


''' 
clients += client_name
UnboundLocalError: local variable 'clients' referenced before assignment

La solución es agregar el keyword 'global' clients
 '''

def create_client(client):
    global clients

    """ if client not in clients:
        # clients += client
        # _add_comma()
        clients.append(client) """

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    """ global clients
    print(clients)
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client)) """
    
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name = client['name'], 
            company = client['company'], 
            email = client['email'],
            position = client['position']
        ))


def update_client(client_id, updated_client):
    global clients

    """ if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
        index = clients.index(client_name)
        clients[index] = updated_name """

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else: 
        print('Client is not in the client\'s list')


def delete_client(client_id):
    global clients

    """ if client_name in clients:
        clients = clients.replace(client_name + ',', '')
        clients.remove(client_name)
    else: 
        print('Client is not in the clients list') """
    
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break

def search_client(client_name):
    # client_list = clients.split(',')

    # for client in client_list:
    for client in clients:    
        # if client != client_name:
        if client['name'] != client_name:
            continue
        else:
            return True

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client

""" def _add_comma():
    global clients
    clients += ',' """


def _print_welcome():
    print('WELCOME TO TIENDA VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field



def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client client?')

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
        """ client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        } """
        # client_name = _get_client_name()
        # create_client(client_name)

        client = _get_client_from_user()
        create_client(client)
        list_clients()

    elif command == 'L':
        list_clients()
    elif command == 'U':
        """ client_name = _get_client_name()
        updated_name = input('What is the updated client name? ')
        update_client(client_name, updated_name) """
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()
    elif command == 'D':
        """ client_name = _get_client_name()
        delete_client(client_name) """

        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'S':
        # client_name = _get_client_name()
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list.')
        else:
            # {} = placeholder
            print('The client: {} is not in our client\'s list.'.format(client_name))

    else:
        print('Invalid command')