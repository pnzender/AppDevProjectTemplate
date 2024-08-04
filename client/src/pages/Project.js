import React, { useState } from 'react';

function ProjectForm() {
  const [newProject, setNewProject] = useState({
    name: '',
    description: '',
    projectId: ''
  });
  const [existingProjectId, setExistingProjectId] = useState('');
  const [response, setResponse] = useState('');

  const handleNewProjectChange = (e) => {
    setNewProject({ ...newProject, [e.target.name]: e.target.value });
  };

  const handleExistingProjectChange = (e) => {
    setExistingProjectId(e.target.value);
  };

  const handleCreateNewProject = async () => {
    try {
      const res = await fetch('/create_project', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newProject),
      });

      const data = await res.json();
      if (res.ok) {
        setResponse(data.message);
        alert(data.message)
        setNewProject({
          name: '',
          description: '',
          projectId: '',
        });
      } else {
        setResponse('Error creating project.');
        alert('Error retrieving project.');
      }
    } catch (error) {
      console.error(error);
      setResponse('Error creating project.');
      alert('Error creating project.');
    }
  };

  const handleUseExistingProject = async () => {
    try {
      const res = await fetch(`http://localhost:5000/api/projects/${existingProjectId}`);

      const data = await res.json();
      if (res.ok) {
        setResponse(data.message);
      } else {
        setResponse('Error retrieving project.');
      }
    } catch (error) {
      console.error(error);
      setResponse('Error retrieving project.');
    }
  };

  return (
    <div style={{ display: 'flex' }}>
      <div style={{ flex: 1, padding: '10px' }}>
        <h2>Create New Project</h2>
        <label>
          Name:
          <input
            type="text"
            name="name"
            value={newProject.name}
            onChange={handleNewProjectChange}
          />
        </label>
        <br />
        <label>
          Description:
          <textarea
            name="description"
            value={newProject.description}
            onChange={handleNewProjectChange}
          />
        </label>
        <br />
        <label>
          Project ID:
          <input
            type="text"
            name="projectId"
            value={newProject.projectId}
            onChange={handleNewProjectChange}
          />
        </label>
        <br />
        <button onClick={handleCreateNewProject}>Create Project</button>
      </div>
      <div style={{ flex: 1, padding: '10px' }}>
        <h2>Use Existing Project</h2>
        <label>
          Project ID:
          <input
            type="text"
            value={existingProjectId}
            onChange={handleExistingProjectChange}
          />
        </label>
        <br />
        <button onClick={handleUseExistingProject}>Use Project</button>
      </div>
    </div>
  );
}

export default ProjectForm;
