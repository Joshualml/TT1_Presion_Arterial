// UserProfile.tsx
import React, { useState, useEffect } from 'react';

interface Measurement {
  presion_sistolica: number;
  presion_diastolica: number;
}

const UserProfile: React.FC = () => {
  const [measurements, setMeasurements] = useState<Measurement[]>([]);

  useEffect(() => {
    const fetchMeasurements = async () => {
      try {
        const response = await fetch('http://localhost:8000/data_user/1'); // Cambia el ID según el usuario
        if (response.ok) {
          const data = await response.json();
          setMeasurements(data);
        }
      } catch (error) {
        console.error('Error al cargar mediciones:', error);
      }
    };
    fetchMeasurements();
  }, []);

  return (
    <div>
      <h2>Perfil de Usuario</h2>
      <h3>Mediciones de Presión</h3>
      <ul>
        {measurements.map((measurement, index) => (
          <li key={index}>
            Presión Sistólica: {measurement.presion_sistolica}, Presión Diastólica: {measurement.presion_diastolica}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserProfile;
