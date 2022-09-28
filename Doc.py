class Doc:
  def __init__(self):
    self.tipoDoc = ""
    self.fechaInicioDoc = ""
    self.fechaFinDoc = ""
    self.observacionesDoc = ""

  def __str__(self):
    print("Tipo documentación: " + self.tipoDoc)
    print("Fecha de inicio: " + self.fechaInicioDoc)
    print("Fecha de cierre: " + self.fechaFinDoc)
    print("Observaciones: " + self.observacionesDoc)

  def get_tipo(self):
    return self.tipoDoc
  def get_fecha_inicio_doc(self):
    return self.fechaInicioDoc
  def get_fecha_fin_doc(self):
    return self.fechaFinDoc
  def get_obs_doc(self):
    return self.observacionesDoc