import { useState } from "react";
import "./Facturacion.css";
import NuevaVenta from "./NuevaVenta";

const Facturacion = () => {

  return (
    <>
    <div className="container">
      <div className="d-flex justify-content-between aling-items-center p-3">
        <h3>Facturas</h3>
        <button className="btn btn-success" data-bs-toggle="modal" data-bs-target="#nuevaVenta">Nueva Venta</button>
      </div>
    </div>  
    <div class="modal fade" id="nuevaVenta" tabIndex="-1">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-fullscreen" role="document">
        <div class="modal-content">
          <div class="modal-header bg-success text-light" data-bs-theme="dark">
            <h5 class="modal-title" id="modalTitleId">Nueva Venta</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <NuevaVenta/>
          </div>
        </div>
      </div>
    </div>

    </>
  );
};

export default Facturacion;
