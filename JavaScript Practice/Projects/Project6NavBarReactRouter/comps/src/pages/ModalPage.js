import { useState } from 'react';
import Modal from '../components/Modal';
import Button from '../components/Button';

function ModalPage() {
    const [showModal, setShowModal] = useState(false);

    const handleClick = () => {
        setShowModal(true);
    }

    return (
        <div className='relative'>
            <Button onClick={handleClick} primary>OpenModal</Button>
            {showModal && <Modal />}
        </div>
    )
}

export default ModalPage;