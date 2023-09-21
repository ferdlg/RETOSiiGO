import Swal from "sweetalert2"
import withReactContent from "sweetalert2-react-content"

export function showAlert(i, title, text){
    const MySwal = withReactContent(Swal);
    MySwal.fire({
        title:title,
        text:text,
        icon:i
    });
}

export const formatPesos = (valor) => {
    const formatter = new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP',
    });

    return formatter.format(valor);
};

export const formatFecha= (datetime) => {
    const dateObj = new Date(datetime);
    const fecha = dateObj.toISOString().split('T')[0];

    return fecha;
}

export const formatHora = (datetime) => {
    const dateObj = new Date(datetime);
    const horas = dateObj.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });

    return horas;
  }