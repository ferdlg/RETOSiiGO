import "./Inventario.css"

const Inventario = () =>{
    const productos = [1,2,3,4,5,6,7,8]
    return (
        <div className="container">
            <div className="d-flex justify-content-between align-items-center">
                <h2 className="my-3">Inventario</h2>
                <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#agregarProducto">
                    <i class="fa-regular fa-plus me-2"></i>
                    Agregar Producto
                </button>
            </div>
            <div className="d-flex aling-items-center justify-content-center gap-3 flex-wrap">
                {
                    productos.map((producto)=>(
                        <div class="card border-success cardProducto">
                            <div class="card-body">
                                <h4 class="card-title">Titulo producto {producto}</h4>
                                <span class="card-text">Existencias {producto}</span>
                            </div>
                            <div class="card-footer">
                                <button class="btn btn-success float-end" data-bs-toggle="modal" data-bs-target="#editarProducto">
                                    <i class="fa-regular fa-edit"></i>
                                </button>
                            </div>
                        </div>
                    ))
                }
            </div>
            
            <div class="modal fade" id="agregarProducto" tabIndex="-1" role="dialog" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                            <div class="modal-header">
                                    <h5 class="modal-title text-success" id="modalTitleId">Nuevo Producto</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                        <div class="modal-body">
                            <div class="input-group mb-3">
                                <span class="input-group-text"><i className="fa-solid fa-tag pe-2"></i>Producto:</span>
                                <input type="text" class="form-control" placeholder="Producto"/>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-success">Guardar</button>
                        </div>
                    </div>
                </div>
            </div>                     
            <div class="modal fade" id="editarProducto" tabIndex="-1" role="dialog" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                            <div class="modal-header">
                                    <h5 class="modal-title" id="modalTitleId"><span className="text-success">Producto: </span>Nombre Producto</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                        <div class="modal-body">
                            <div class="input-group mb-3">
                                <span class="input-group-text"><i className="fa-solid fa-tag pe-2"></i>Producto:</span>
                                <input type="text" class="form-control" placeholder="Producto"/>
                            </div>
                            <div class="input-group mb-3">
                                <span class="input-group-text">
                                    <i className="fa-solid fa-list pe-2"></i>
                                    Existencias Actuales:
                                </span>
                                <input type="number" disabled class="form-control" placeholder="Producto" value="5"/>
                            </div>
                            <div class="input-group mb-3">
                                <span class="input-group-text">
                                    <i className="fa-solid fa-minus pe-2"></i>
                                    Restar:
                                </span>
                                <input type="number" class="form-control" placeholder="Producto" value="0"/>
                                <span class="input-group-text">
                                    <i className="fa-solid fa-plus pe-2"></i>
                                    Agregar:
                                </span>
                                <input type="number" class="form-control" placeholder="Producto" value="0"/>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-success">Guardar</button>
                        </div>
                    </div>
                </div>
            </div>                     
        </div>
    )
}

export default Inventario;