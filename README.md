<div align="center">
  <h1>🚀 Employee Management REST API</h1>
  
  <p><em>Built with Django REST Framework & MySQL</em></p>
</div>

<hr />

<h2>📌 Project Objective</h2>
<p>
  This project implements a secure RESTful API to manage company employees. It covers full CRUD operations, 
  JWT authentication, and strict adherence to RESTful principles as outlined in the project requirements.
</p>



<h2>🛠️ Tech Stack</h2>
<ul>
  <li><b>Framework:</b> Django REST Framework (DRF) [cite: 5]</li>
  <li><b>Database:</b> MySQL [cite: 5]</li>
  <li><b>Authentication:</b> SimpleJWT (Token-based) </li>
  <li><b>Testing:</b> Django APITestCase </li>
</ul>

<h2>🚦 Setup & Installation</h2>

<h3>1. Environment Setup</h3>
<pre><code>git clone &lt;your-repo-url&gt;
cd habot-backend-project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt</code></pre>

<h3>2. Database Configuration</h3>
<p>Ensure you have a MySQL database created. Update the <code>DATABASES</code> section in <code>core/settings.py</code>[cite: 5]:</p>
<pre><code>'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'habot_db',
    'USER': 'your_user',
    'PASSWORD': 'your_password',
}</code></pre>

<h3>3. Initialization</h3>
<pre><code>python manage.py migrate
python manage.py createsuperuser
python manage.py runserver</code></pre>

<h2>📖 API Documentation</h2>
<table width="100%">
  <thead>
    <tr>
      <th>Method</th>
      <th>Endpoint</th>
      <th>Description</th>
      <th>Status Code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>POST</code></td>
      <td>/api/token/</td>
      <td>Obtain JWT Access Token </td>
      <td>200 OK</td>
    </tr>
    <tr>
      <td><code>POST</code></td>
      <td>/api/employees/</td>
      <td>Create new employee </td>
      <td>201 Created</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td>/api/employees/</td>
      <td>List all (10 per page) </td>
      <td>200 OK</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td>/api/employees/{id}/</td>
      <td>Retrieve single employee </td>
      <td>200 / 404</td>
    </tr>
    <tr>
      <td><code>PUT</code></td>
      <td>/api/employees/{id}/</td>
      <td>Update details </td>
      <td>200 OK</td>
    </tr>
    <tr>
      <td><code>DELETE</code></td>
      <td>/api/employees/{id}/</td>
      <td>Remove record </td>
      <td>204 No Content</td>
    </tr>
  </tbody>
</table>

<h2>🧪 Quality Assurance</h2>
<ul>
  <li><b>Testing:</b> Run <code>python manage.py test</code> to execute unit tests for all endpoints.</li>
  <li><b>Validation:</b> Includes unique email checks and name-field requirements.</li>
  <li><b>Filtering:</b> Supports <code>?department=</code> and <code>?role=</code> queries.</li>
</ul>

<hr />

<div align="center">
  <p>Developed to demonstrate <b>Leadership Principles</b> and <b>Technical Excellence</b>[cite: 2, 5].</p>
</div>
