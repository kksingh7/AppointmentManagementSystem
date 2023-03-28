import React, {useState} from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";

let doctors=['Hema','Rekha'];
let patients=['Sushma','Pasandida','Nirma'];

function App() {

    const [show, setShow] = useState(false);
    const [isDoctor, setIsDoctor]=useState(true);
    const [Dlist, setDlist]=useState(doctors);
    const [Plist, setPlist]=useState(patients);
    const [personName,setPersonName]=useState('');


  const setDoctor =()=>setIsDoctor(true);
  const setPatient=()=>setIsDoctor(false);
  const handleClose = () => setShow(false);
  const handleShow =(isDoctor,pName)=> () => {
    if(isDoctor)
        setDoctor();
    else
        setPatient();
    setPersonName(pName);
    setShow(true);
  }

    const renderHeadCell=(headerName)=>{
        return (
            <div style={{
                 display: 'flex',
                 flex:1,
            alignItems: 'center',
            justifyContent: 'center',
            }}>
                <h4>{headerName}</h4>
                <div style={{marginLeft: 20}}>
                    <Button variant="primary" onClick={()=>{}}>+</Button>
                </div>
            </div>
        );
    };

    const renderDivider=()=>{
        return (
            <div style={{width: 30,border: '1px solid black'}}></div>
        );
    };

	const renderHeader=()=>{
        return (
            <div style={{
                display:'flex',
                flexDirection:'row',
                marginBottom: 20,
                border: '2px solid black'
            }}>
                {renderHeadCell('Doctor')}
                {renderDivider()}
                {renderHeadCell('Patient')}
            </div>
        )
    };

    const removeEntity=(isDoctor, data)=>()=>{
        if (isDoctor) {
            doctors = doctors.filter(arr => arr != data);
            setDlist(doctors)
        } else  {
            patients = patients.filter(arr => arr != data);
            setDlist(patients)
        }
    }

    const renderCell=(data, isDoctor)=>{
        if(data==='')
            return (
                <div style={{flex:1}}></div>
            );
        return (
            <div style={{
                 display: 'flex',
                 flex:1,
            alignItems: 'center',
            justifyContent: 'center',
            border: '1px solid black',
                flexDirection: 'row'
            }}>
            <Button variant="primary" onClick={handleShow(isDoctor,data)}>
        <h6>{data}</h6>
      </Button>
                <div style={{marginLeft: 20}}>
                    <Button variant="primary" onClick={removeEntity(isDoctor, data)}>X</Button>
                </div>
            </div>
        );
    };

    const renderRow=(doctor,patient)=>{
        return (
        <div key={doctor+'$'+patient} style={{
                display:'flex',
                flexDirection:'row',
                marginBottom: 20,}}>
            {renderCell(doctor,true)}
            {renderDivider()}
            {renderCell(patient,false)}
        </div>
        );
    };

    const renderRows=()=>{
        const maxIndex=Math.max(doctors.length,patients.length);
        const rows=[];
        for(let i=0;i<maxIndex;i++){
            const doctor=i<doctors.length?doctors[i]:'';
            const patient=i<patients.length?patients[i]:'';
            rows.push(renderRow(doctor,patient));
        }
        return (
            <div>
                {rows}
            </div>
        );
    };

    const addAppointment=()=>{
       return( <div>
            <Button variant="primary" onClick={()=>{}}>Add Appointment</Button>
        </div>
       );
    }

    const renderDetails = ()=>{

        const heading=isDoctor?'Doctors details':'Patient Details';

   return (
            <div>
                <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>{heading}</Modal.Title>
        </Modal.Header>
        <Modal.Body>{personName}</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
            </div>
        )
    };

    return (
        <div>
        {renderHeader()}
        {renderDetails()}
        {renderRows()}
            {addAppointment()}
        </div>
    )
}

export default App;