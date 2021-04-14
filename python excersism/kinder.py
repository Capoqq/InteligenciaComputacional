class Garden:
    def __init__(self, diagrama, estudiantes=[]):
        self.plants_row_1, self.plants_row_2 = diagrama.split('\n')

        if len(estudiantes) == 0:
            estudiantes = ['Alice',  'Bob',    'Charlie', 'David', 
                        'Eve',    'Fred',   'Ginny',   'Harriet', 
                        'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.estudiantes = sorted(estudiantes)

        self.plant_names = {'C': 'Clover',
                            'G': 'Grass',
                            'R': 'Radishes',
                            'V': 'Violets'}


    def plants(self, nombre_estudiante):
        index = self.estudiantes.index(nombre_estudiante) * 2
        plantas_iniciales = self.plants_row_1[index:index+2] + self.plants_row_2[index:index+2]
        return [self.plant_names[initial] for initial in plantas_iniciales]