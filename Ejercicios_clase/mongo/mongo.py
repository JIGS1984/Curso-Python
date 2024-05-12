from pymongo import MongoClient

cliente = MongoClient('localhost')
db = cliente['nueva']
col = db['personas']
col.insert_one({
        'edad':20,
        'nombre':'Leonardo',
        'intereses':['Musica','youtube']
    })
col.insert_many([
    {
        'edad':20,
        'nombre':'Leonardo',
        'intereses':['Musica','youtube']
    },
    {
        'edad':20,
        'nombre':'Leonardo',
        'intereses':['Musica','youtube']
    },
    {
        'edad':20,
        'nombre':'Leonardo',
        'intereses':['Musica','youtube']
    },
    
    {
        'edad':20,
        'nombre':'Leonardo',
        'intereses':['Musica','youtube']
    }
    ])

print(col.count_documents({}))
print(cliente.list_database_names())
print(db.list_collection_names())
for documento in col.find({}):
    print(documento)
for documento in col.find({
     'edad':{
          '$gt':20
         }

    }):
    print(documento)
