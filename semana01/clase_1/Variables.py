personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]

print(personas[0]['nacionalidad'])
print(personas[0]['hobbies'][1]['experiencia'])

print(personas[1]['hobbies'][0]['nombre'])
print(personas[1]['hobbies'][1]['nombre'])