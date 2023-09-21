import { DataGrid } from '@mui/x-data-grid';
import { formatPesos, formatFecha, formatHora } from '../../../utilities';
import { Autocomplete, TextField } from '@mui/material';
import "./Facturas.css";

const Facturas = () => {
  const columnsFacturas = [
    { 
      field: 'id', 
      headerName: 'ID', 
      headerAlign: "center",
      align: "center",
      flex: 1,
    },
    { 
      field: 'fecha', 
      headerName: 'Fecha', 
      flex: 1,
      valueFormatter: (params) => formatFecha(params.value),
    },
    { 
      field: 'hora', 
      headerName: 'Hora', 
      headerAlign: "center",
      align: "center",
      flex: 1,
      valueFormatter: (params) => formatHora(params.value),
    },
    { 
      field: 'total', 
      headerName: 'Total', 
      headerAlign: "center",
      align: "center",
      flex: 1,
      valueFormatter: (params) => formatPesos(params.value),
    },
    {
      field: 'acciones',
      headerName: '',
      sortable: false,
      filterable: false, 
      width: 40,
      headerAlign: "center",
      align: "center",
      renderCell: (params) => (
        <button className='btn_outline_azulClaro'>
          Ver
        </button>
      ),
    },
  ];
  
  const rowsFacturas = [
    { id: 1, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 2, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 3, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 4, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 5, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 6, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 7, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 8, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 9, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 10, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 11, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 12, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 13, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 14, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 15, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 16, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
    { id: 17, fecha: '2023-09-15 10:00:00', hora: '2023-09-15 10:00:00', total: 50000 },
  ];

  const prodcuts = [
    {label:"Producto 1"},
    {label:"Producto 2"},
    {label:"Producto 3"},
    {label:"Producto 4"},
    {label:"Producto 5"},
    {label:"Producto 6"},
    {label:"Producto 7"},
    {label:"Producto 8"},
    {label:"Producto 9"},
    {label:"Producto 10"},
    {label:"Producto 11"},
  ]

    // Generar filas para la tabla modal usando map
    const rowsModal = Array.from({ length: 50 }, (_, index) => ({
      id: index + 1,
      producto: `Producto ${index + 1}`,
      cantidad: 4,
      pUnitario: "$10.000",
      total: "$40.000",
      iva: "$7.600",
    }));

  return (
    <div className='containerFacturas'>
      <div className='d-flex justify-content-between align-items-center my-4'>
        <h1>Facturas</h1>
        <button className='btn_outline_azulOscuro px-5' data-bs-toggle="modal" data-bs-target="#nuevaFactura">+ Nueva</button>
      </div>
      <table>

      </table>
      <div className='tablaFacturas'>
        <DataGrid
          rows={rowsFacturas}
          columns={columnsFacturas}
          initialState={{
            pagination: {
              paginationModel: { page: 0, pageSize: 5 },
            },
          }}
          pageSizeOptions={[5, 10]}
          stickyHeader
        />

    </div>
      {/* Modal de nueva factura */}
      <div className="modal fade" id="nuevaFactura" tabIndex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
        <div className="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-xl" role="document">
          <div className="modal-content">
            <div className="modal-header bg_azulOscuro text-light">
              <h5 className="modal-title" id="modalTitleId">Nueva Factura</h5>
              <button type="button" className="btn-close bg_blanco" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              <div className='tablaAgregarProductos overflow-auto border_azulOscuro'>
                <table className="table table-hover text-center">
                  <thead className='sticky-top'>
                    <tr>
                      <th scope="col">ID</th>
                      <th scope="col">Producto</th>
                      <th scope="col">Cantidad</th>
                      <th scope="col">P.Unitario</th>
                      <th scope="col">Total</th>
                      <th scope="col">IVA</th>
                    </tr>
                  </thead>
                  <tbody>
                    {rowsModal.map((row) => (
                      <tr key={row.id}>
                        <th scope="row">{row.id}</th>
                        <td>{row.producto}</td>
                        <td>
                          <button className='btn_outline_azulOscuro mx-2'>
                            -
                          </button>
                          {row.cantidad}
                          <button className='btn_outline_azulOscuro mx-2'>
                            +
                          </button>
                        </td>
                        <td>{row.pUnitario}</td>
                        <td>{row.total}</td>
                        <td>{row.iva}</td>
                        <td>
                          <button className='btn_outline_naranja mx-2'>
                            X
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <div className='border_azulOscuro p-3 d-flex justify-content-between align-items-center'>
                <button className='btn_azulOscuro' data-bs-toggle="modal" data-bs-target="#agregarProducto">Agregar Producto</button>
                <div class="input-group w-25">
                  <span class="input-group-text">Total: </span>
                  <input class="form-control" disabled/>
                </div>
              </div>
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
              <button type="button" className="btn btn-primary">Registrar</button>
            </div>
          </div>
        </div>
      </div>
      {/* Modal de agregar producto a Factura */}
      <div className="modal fade" id="agregarProducto" tabIndex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
        <div className="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-s" role="document">
          <div className="modal-content">
            <div className="modal-header bg_azulOscuro text-light">
              <h5 className="modal-title" id="modalTitleId">Agregar Producto</h5>
              <button type="button" className="btn-close bg_blanco" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              <div className='border_azulOscuro p-3 d-flex justify-content-center align-items-center'>
              <Autocomplete
                id="combo-box-demo"
                options={prodcuts}
                sx={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Producto" />}
              />
              </div>
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
              <button type="button" className="btn btn-primary">Agregar</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Facturas;

