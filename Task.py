class Task:
  def __init__(self, id):
    self.id = id
    self.fechaCreacion = ""
    self.fechaCierre = ""
    self.docs = []

  def __str__(self):
    return r"ID Tarea: {self.id}"

  def display(self):
    print("ID Tarea: {}".format(self.id))
    print("Fecha creación: {self.fechaCreacion}")
    i = 1
    for x in self.docs:
      print("Doc " + i)
      print(x)
      i+=1
    print("Fecha cierre: {self.fechaCierre}")


  def get_id(self):
    return self.id
  def get_fecha_creacion(self):
    return self.fechaCreacion
  def get_fecha_cierre(self):
    return self.fechaCierre
  def get_docs(self):
    return self.docs

  def set_id(self, id):
    self.id = id
  def set_fecha_creacion(self, fechaCreacion):
    self.fechaCreacion = fechaCreacion
  def set_fecha_cierre(self, fechaCierre):
    self.fechaCierre = fechaCierre
  def set_docs(self, docs):
    self.docs = docs

  # def to_json(self):
  #   jsonDocs = [
  #     {
        
  #     }
  #   ]
  #   jsonTask = {
  #     "id": self.get_id(),
  #     "fechaInicio": "",
  #     "fechaFin": "",
  #     "observaciones": ""
  #   }

  # def load_from_file():
    