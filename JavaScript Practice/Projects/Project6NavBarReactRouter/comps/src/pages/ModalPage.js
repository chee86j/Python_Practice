import { useState } from 'react';
import Modal from '../components/Modal';
import Button from '../components/Button';

function ModalPage() {
  const [showModal, setShowModal] = useState(false);

  const handleClick = () => {
    setShowModal(true);
  };

  const handleClose = () => {
    setShowModal(false);
  };

  const actionBar = (
    <div>
      <Button onClick={handleClose} primary>
        I Accept
      </Button>
    </div>
  );

  const modal = (
    <Modal onClose={handleClose} actionBar={actionBar}>
      <p>Here is an important agreement for you to accept.</p>
    </Modal>
  );

  return (
    <div>
      
      <Button onClick={handleClick} primary>
        OpenModal
      </Button>
      {showModal && modal}
      
      <p>
        Sunt elit sit id veniam ad sit duis sunt do qui minim aliquip. Nulla quis id proident dolor amet laboris proident adipisicing. Nulla ea id irure magna ut nostrud cupidatat. Nisi enim quis aliqua non reprehenderit amet amet anim consectetur aliqua. Laborum elit nulla duis proident est do sit duis commodo eiusmod est officia. Occaecat aliqua commodo est aliqua tempor ex aute est.
      </p>
      <p>
        Lorem ipsum labore non eiusmod eu commodo ea do nulla mollit esse qui ea. Laboris consectetur elit exercitation reprehenderit eiusmod pariatur aliqua est. Ex culpa velit labore sint pariatur id dolor magna amet sint esse nostrud ut mollit. Amet occaecat magna voluptate incididunt non anim ipsum do incididunt culpa. Labore enim ea sint eu.
      </p>
      <p>
        Laboris dolor laboris labore do nisi aute veniam ullamco. Non qui fugiat officia id mollit aliqua sunt deserunt exercitation ad quis officia. Aute occaecat sit mollit ad reprehenderit mollit laborum pariatur ex.
      </p>
      <p>
        Sunt elit sit id veniam ad sit duis sunt do qui minim aliquip. Nulla quis id proident dolor amet laboris proident adipisicing. Nulla ea id irure magna ut nostrud cupidatat. Nisi enim quis aliqua non reprehenderit amet amet anim consectetur aliqua. Laborum elit nulla duis proident est do sit duis commodo eiusmod est officia. Occaecat aliqua commodo est aliqua tempor ex aute est.
      </p>
      <p>
        Lorem ipsum labore non eiusmod eu commodo ea do nulla mollit esse qui ea. Laboris consectetur elit exercitation reprehenderit eiusmod pariatur aliqua est. Ex culpa velit labore sint pariatur id dolor magna amet sint esse nostrud ut mollit. Amet occaecat magna voluptate incididunt non anim ipsum do incididunt culpa. Labore enim ea sint eu.
      </p>
      <p>
        Laboris dolor laboris labore do nisi aute veniam ullamco. Non qui fugiat officia id mollit aliqua sunt deserunt exercitation ad quis officia. Aute occaecat sit mollit ad reprehenderit mollit laborum pariatur ex.
      </p>
      <p>
        Sunt elit sit id veniam ad sit duis sunt do qui minim aliquip. Nulla quis id proident dolor amet laboris proident adipisicing. Nulla ea id irure magna ut nostrud cupidatat. Nisi enim quis aliqua non reprehenderit amet amet anim consectetur aliqua. Laborum elit nulla duis proident est do sit duis commodo eiusmod est officia. Occaecat aliqua commodo est aliqua tempor ex aute est.
      </p>
      <p>
        Lorem ipsum labore non eiusmod eu commodo ea do nulla mollit esse qui ea. Laboris consectetur elit exercitation reprehenderit eiusmod pariatur aliqua est. Ex culpa velit labore sint pariatur id dolor magna amet sint esse nostrud ut mollit. Amet occaecat magna voluptate incididunt non anim ipsum do incididunt culpa. Labore enim ea sint eu.
      </p>
      <p>
        Laboris dolor laboris labore do nisi aute veniam ullamco. Non qui fugiat officia id mollit aliqua sunt deserunt exercitation ad quis officia. Aute occaecat sit mollit ad reprehenderit mollit laborum pariatur ex.
      </p>
      <p>
        Sunt elit sit id veniam ad sit duis sunt do qui minim aliquip. Nulla quis id proident dolor amet laboris proident adipisicing. Nulla ea id irure magna ut nostrud cupidatat. Nisi enim quis aliqua non reprehenderit amet amet anim consectetur aliqua. Laborum elit nulla duis proident est do sit duis commodo eiusmod est officia. Occaecat aliqua commodo est aliqua tempor ex aute est.
      </p>
      <p>
        Lorem ipsum labore non eiusmod eu commodo ea do nulla mollit esse qui ea. Laboris consectetur elit exercitation reprehenderit eiusmod pariatur aliqua est. Ex culpa velit labore sint pariatur id dolor magna amet sint esse nostrud ut mollit. Amet occaecat magna voluptate incididunt non anim ipsum do incididunt culpa. Labore enim ea sint eu.
      </p>
      <p>
        Laboris dolor laboris labore do nisi aute veniam ullamco. Non qui fugiat officia id mollit aliqua sunt deserunt exercitation ad quis officia. Aute occaecat sit mollit ad reprehenderit mollit laborum pariatur ex.
      </p>

    </div>
  );
}

export default ModalPage;
