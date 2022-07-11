
def print_hi(name):

    print(f'Hi, {name}')



if __name__ == '__main__':
    print_hi('ola cleverson')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import mysql.connector
banco = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "",
    database = "DBcentral"
)
dados=()
print(dados)
#cursor = banco.cursor()
#comando_sql = "INSERT into pessoas (nome,idade,email) VALUES (%s,%s,%s)"

#cursor.execute(comando_sql,dados)
#banco.commit()
