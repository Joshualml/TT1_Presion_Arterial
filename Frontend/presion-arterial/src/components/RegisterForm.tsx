import React, { useState } from 'react'; 

const RegisterForm: React.FC = () => {
  const [nombre, setNombre] = useState<string>('');
  const [contraseña, setContraseña] = useState<string>('');
  const [edad, setEdad] = useState<number | ''>('');  // Permite vacío y número
  const [message, setMessage] = useState<string>('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const userData = {
      nombre: nombre,
      contraseña: contraseña,
      edad: edad,  // Convertir edad a número entero si no está vacío
    };
    console.log(userData);

    try {
      const response = await fetch('http://localhost:8000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      if (response.ok) {
        const data = await response.json();
        setMessage('Usuario registrado exitosamente');
        console.log(data);
      } else {
        setMessage('Error al registrar usuario');
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      setMessage('Error de conexión con la API');
      console.error('Error de conexión:', error);
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto' }}>
      <h2>Registro de Usuario</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nombre:</label>
          <input
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Contraseña:</label>
          <input
            type="password"
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Edad:</label>
          <input
            type="number"
            value={edad}
            onChange={(e) => setEdad(e.target.value === '' ? '' : parseInt(e.target.value))}
            required
          />
        </div>
        <button type="submit">Registrar</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default RegisterForm;
