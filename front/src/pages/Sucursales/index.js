import { useEffect, useState } from 'react';
import apiService from '../../Services';
import "./Sucursales.css";

const Sucursales = () => {
  const [sucursales, setSucursales] = useState([]);

  const [id_sucursal, setid_sucursal] = useState();
  const [nombre_sucursal, setnombre_sucursal] = useState();
  const [ciudad, setciudad] = useState();
  const [direccion, setdireccion] = useState();
  const [email, setemail] = useState();
  const [estado_inactiva, setestado_inactiva] = useState();
  const [id_bodega_fk, setid_bodega_fk] = useState();

  useEffect(()=>{
    apiService.getSucursales()
    .then((data) => {
      setSucursales(data);
      console.log(sucursales)
    })
    .catch((e) => {
        console.error('FRONT ERROR. Sucursales: ' + e);
    });
  },[])
  

  return (
    <>
        <div className="container">
        <div className="d-flex justify-content-between align-items-center my-3">
          <h1>Sucursales</h1>
          <button className="btn_azulOscuro" data-bs-toggle="modal" data-bs-target="#nuevaSucursal">
            + Nueva
          </button>
        </div>
        <div className='tablaSucursales overflow-auto border_azulOscuro'>
                <table className="table table-hover text-center">
                  <thead className='sticky-top'>
                    <tr>
                      <th scope="col">ID</th>
                      <th scope="col">Nombre</th>
                      <th scope="col">Ciudad</th>
                      <th scope="col">Dirección</th>
                      <th scope="col">Email</th>
                      <th scope="col">Opciones</th>
                    </tr>
                  </thead>
                  <tbody>
                    {sucursales.map((row) => (
                      <tr key={row.id}>
                        <th scope="row">{row.id_sucursal}</th>
                        <td>{row.nombre_sucursal}</td>
                        <td>{row.ciudad}</td>
                        <td>{row.direccion}</td>
                        <td>{row.email}</td>
                        <td>
                          <button className='btn_outline_azulClaro mx-2'>
                            <i className='fa-solid fa-edit'></i>
                          </button>
                          <button className='btn_outline_azulClaro mx-2' data-bs-toggle="modal" data-bs-target="#empleadosSucursal">
                            <i className='fa-solid fa-user-tie'></i>
                          </button>
                          <button className='btn_outline_azulClaro mx-2'>
                            <i class="fa-solid fa-file-invoice-dollar"></i>
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
    </div>
    {/* Modal Nueva Sucursal */}
    <div class="modal fade" id="nuevaSucursal" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-lg" role="document">
        <div class="modal-content">
          <div class="modal-header bg_azulOscuro color_blanco">
            <h5 class="modal-title" id="modalTitleId">Nueva Sucursal</h5>
              <button type="button" class="btn-close bg_blanco" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
          <div className='d-flex gap-2'>
            <div class="input-group w-50 mb-3">
              <span class="input-group-text w-25">Nombre:</span>
              <input type="text" class="form-control" placeholder="Nombre"/>
            </div>
            <div class="input-group w-50 mb-3">
              <span class="input-group-text w-25">Ciudad:</span>
              <input type="text" class="form-control" placeholder="Ciudad"/>
            </div>
          </div>
          <div className='d-flex gap-2'>
            <div class="input-group w-50 mb-3">
              <span class="input-group-text w-25">Dirección:</span>
              <input type="text" class="form-control" placeholder="Dirección"/>
            </div>
            <div class="input-group w-50 mb-3">
              <span class="input-group-text w-25">Email:</span>
              <input type="text" class="form-control" placeholder="Email"/>
            </div>
          </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="button" class="btn btn-primary">Guardar</button>
          </div>
        </div>
      </div>
    </div>
    {/* Modal empleados Sucursal */}
    <div class="modal fade" id="empleadosSucursal" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-xl" role="document">
        <div class="modal-content">
          <div class="modal-header bg_azulOscuro color_blanco">
            <h5 class="modal-title" id="modalTitleId">Empleados Sucursal</h5>
              <button type="button" class="btn-close bg_blanco" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
          <div className='d-flex gap-2'>
            <div class="input-group w-50 mb-3">
              <input type="text" class="form-control" placeholder="Producto"/>
              <span class="input-group-text w-25 btn_azulOscuro">
                <button className='btn_azulOscuro w-100'>
                  Agregar
                </button>
              </span>
            </div>
            <div class="input-group w-50 mb-3">
              <input type="text" class="form-control" placeholder="Producto"/>
              <span class="input-group-text w-25 btn_azulOscuro">
                <button className='btn_azulOscuro w-100'>
                  Buscar
                </button>
              </span>
            </div>
          </div>
          <div className='d-flex gap-2'>
            <div class="input-group w-50 mb-3">
              <span class="input-group-text w-25">Dirección:</span>
              <input type="text" class="form-control" placeholder="Dirección"/>
            </div>
            <div class="input-group w-50 mb-3">
              <span class="input-group-text w-25">Email:</span>
              <input type="text" class="form-control" placeholder="Email"/>
            </div>
          </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="button" class="btn btn-primary">Guardar</button>
          </div>
        </div>
      </div>
    </div>
    </>
  )
}

export default Sucursales
