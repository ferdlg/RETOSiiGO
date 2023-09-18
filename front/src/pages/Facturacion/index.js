import { useState } from "react";
import "./Facturacion.css";

const Facturacion = () => {
  const productos = [
    { id: 1, nombre: "Producto 1", existencias: 5 },
    { id: 2, nombre: "Producto 2", existencias: 3 },
    { id: 3, nombre: "Producto 3", existencias: 8 },
    { id: 4, nombre: "Producto 4", existencias: 12 },
    { id: 5, nombre: "Producto 5", existencias: 8 },
    { id: 6, nombre: "Producto 6", existencias: 8 },
    { id: 7, nombre: "Producto 7", existencias: 8 },
    { id: 8, nombre: "Producto 8", existencias: 8 },
    { id: 9, nombre: "Producto 9", existencias: 8 },
  ];

  const [carrito, setCarrito] = useState({});

  const agregarAlCarrito = (producto) => {
    const nuevoCarrito = { ...carrito };

    if (nuevoCarrito[producto.id]) {
      nuevoCarrito[producto.id] += 1;
    } else {
      nuevoCarrito[producto.id] = 1;
    }

    setCarrito(nuevoCarrito);
  };

  const modificarCantidad = (prodId, nuevaCantidad) => {
    const nuevoCarrito = { ...carrito };

    if (nuevaCantidad <= 0) {
      delete nuevoCarrito[prodId];
    } else {
      nuevoCarrito[prodId] = nuevaCantidad;
    }

    setCarrito(nuevoCarrito);
  };

  return (
    <div className="container d-flex">
      <div className="catalogo w-75 d-flex align-items-center justify-content-center gap-3 flex-wrap">
        {productos.map((producto) => (
          <div className="card border-success cardProducto" key={producto.id}>
            <div className="card-body">
              <h4 className="card-title">{producto.nombre}</h4>
              <span className="card-text">Existencias {producto.existencias}</span>
            </div>
            <div className="card-footer">
              <button
                className="btn btn-success float-end"
                onClick={() => {
                  agregarAlCarrito(producto);
                }}
              >
                <i className="fa-regular fa-plus"></i>
              </button>
            </div>
          </div>
        ))}
      </div>
      <div className="carrito bg-body-tertiary border border-success rounded w-25">
        <h3 className="text-success m-2">Compra</h3>
        <div className="containerDetallesCarrito border border-grey">
            {Object.keys(carrito).map((prodId) => (
            <div key={prodId} className="detalleCarrito border border-success m-2">
                <h5>{productos.find((producto) => producto.id === parseInt(prodId)).nombre}</h5>
                <div>
                <button
                    className="btn btn-outline-success"
                    onClick={() => {
                    modificarCantidad(prodId, carrito[prodId] - 1);
                    }}
                >
                    <i className="fa-solid fa-minus"></i>
                </button>
                <p>{carrito[prodId]}</p>
                <button
                    className="btn btn-outline-success"
                    onClick={() => {
                    modificarCantidad(prodId, carrito[prodId] + 1);
                    }}
                >
                    <i className="fa-solid fa-plus"></i>
                </button>
                </div>
            </div>
            ))}
        </div>
        <div className="d-grid gap-2 col-8 mx-auto">
            <button className="btn btn-success">
                Registrar
            </button>
        </div>
      </div>
    </div>
  );
};

export default Facturacion;
