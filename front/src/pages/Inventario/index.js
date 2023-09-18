import { showAlert } from "../../utilities";
import Swal from "sweetalert2";
import withReactContent from "sweetalert2-react-content";
import "./Inventario.css";

const Inventario = () =>{
    const productos = [1,2,3,4,5,6,7,8]
    const editarProducto = () => {
        showAlert("success", "El producto se actualizo")
    }

    const eliminarProducto = () => {
        const MySwal = withReactContent(Swal);
        MySwal.mixin({
            customClass: {
              confirmButton: 'btn btn-success',
              cancelButton: 'btn btn-danger'
            },
            buttonsStyling: false
          })
          
          MySwal.fire({
            title: '¿Está seguro de eliminar el producto?',
            text: "¡No puedes retroceder la acción!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: '¡Si, Eliminarlo!',
            cancelButtonText: '¡No, Cancelar!',
            reverseButtons: true
          }).then((result) => {
            if (result.isConfirmed) {
                MySwal.fire(
                'Eliminado!',
                'Tu producto ya no esta en nuestar base de datos.',
                'success'
              )
            } else if (
              result.dismiss === Swal.DismissReason.cancel
            ) {
                MySwal.fire(
                'Cancelado',
                'Tu producto sigue en el sistema',
                'error'
              )
            }
          })
    }

    return (
        <div className="container">
            <div className="d-flex justify-content-between align-items-center">
                <h2 className="my-3">Inventario</h2>
                <button className="btn btn-success" data-bs-toggle="modal" data-bs-target="#agregarProducto">
                    <i className="fa-regular fa-plus me-2"></i>
                    Agregar Producto
                </button>
            </div>
            <div className="d-flex aling-items-center justify-content-center gap-3 flex-wrap">
                {
                    productos.map((producto)=>(
                        <div className="card border-success cardProducto">
                            <div className="card-body">
                                <h4 className="card-title">Titulo producto {producto}</h4>
                                <span className="card-text">Existencias {producto}</span>
                            </div>
                            <div className="card-footer">
                                <button className="btn btn-success float-end" data-bs-toggle="modal" data-bs-target="#editarProducto">
                                    <i className="fa-regular fa-edit"></i>
                                </button>
                            </div>
                        </div>
                    ))
                }
            </div>
            
            <div className="modal fade" id="agregarProducto" tabIndex="-1" role="dialog" aria-hidden="true">
                <div className="modal-dialog" role="document">
                    <div className="modal-content">
                            <div className="modal-header">
                                    <h5 className="modal-title text-success" id="modalTitleId">Nuevo Producto</h5>
                                        <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                        <div className="modal-body">
                            <div className="input-group mb-3">
                                <span className="input-group-text"><i className="fa-solid fa-tag pe-2"></i>Producto:</span>
                                <input type="text" className="form-control" placeholder="Producto"/>
                            </div>
                        </div>
                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" className="btn btn-success">Guardar</button>
                        </div>
                    </div>
                </div>
            </div>                     
            <div className="modal fade" id="editarProducto" tabIndex="-1" role="dialog" aria-hidden="true">
                <div className="modal-dialog" role="document">
                    <div className="modal-content">
                            <div className="modal-header">
                                    <h5 className="modal-title" id="modalTitleId"><span className="text-success">Producto: </span>Nombre Producto</h5>
                                        <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                        <div className="modal-body">
                            <div className="input-group mb-3">
                                <span className="input-group-text"><i className="fa-solid fa-tag pe-2"></i>Producto:</span>
                                <input type="text" className="form-control" placeholder="Producto"/>
                            </div>
                            <div className="input-group mb-3">
                                <span className="input-group-text">
                                    <i className="fa-solid fa-list pe-2"></i>
                                    Existencias Actuales:
                                </span>
                                <input type="number" disabled className="form-control" placeholder="Producto" value="5"/>
                            </div>
                            <div className="input-group mb-3">
                                <span className="input-group-text">
                                    <i className="fa-solid fa-minus pe-2"></i>
                                    Restar:
                                </span>
                                <input type="number" className="form-control" placeholder="Producto" value="0"/>
                                <span className="input-group-text">
                                    <i className="fa-solid fa-plus pe-2"></i>
                                    Agregar:
                                </span>
                                <input type="number" className="form-control" placeholder="Producto" value="0"/>
                            </div>
                        </div>
                        <div className="modal-footer d-flex justify-content-between">
                            <button type="button" className="btn btn-danger" onClick={eliminarProducto}><i className="fa-regular fa-trash-can"></i></button>
                            <div className="d-flex gap-2">
                                <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" className="btn btn-success" onClick={editarProducto}>Guardar</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>                     
        </div>
    )
}

export default Inventario;