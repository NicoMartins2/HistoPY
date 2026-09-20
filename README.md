
  <h1>HistoPY</h1>

  <p>HistoPY is a Python-based utility for reading and displaying command history from the operating system in a unified way.</p>

  <h2>Overview</h2>

  <p>The main objective of HistoPY is to centralize access to the shell history and provide a consistent API for:</p>

  <ul>
    <li>listing all commands</li>
    <li>retrieving the last command</li>
    <li>identifying and displaying commands in a standardized manner</li>
  </ul>

  <p>This project is useful for developers who want to reuse the same logic in both environments without repeating operating system-specific code.</p>

  <h2>Features</h2>

  <ul>
    <li>Cross-platform compatibility between Windows and Linux</li>
    <li>Unified access to command history through a common abstraction</li>
    <li>Support for the main command history files used by each system</li>
    <li>Simple CLI usage through command-line arguments</li>
    <li>Easy extension for new operating systems or shell environments</li>
  </ul>

  <h2>Supported systems</h2>

  <ul>
    <li>Windows</li>
    <li>Linux</li>
  </ul>

  <h2>Installation</h2>

  <ol>
    <li>
      Clone the repository:
      <pre><code>git clone https://github.com/your-user/HistoPY.git</code></pre>
    </li>
    <li>
      Enter the project directory:
      <pre><code>cd HistoPY</code></pre>
    </li>
    <li>
      Run the script with Python:
      <pre><code>python histopy.py</code></pre>
    </li>
  </ol>

  <h2>Usage</h2>

  <p>The project can be executed with the following commands:</p>

  <pre><code>python histopy.py listall
python histopy.py last
python histopy.py id</code></pre>

  <h3>Command descriptions</h3>

  <ul>
    <li><code>listall</code>: displays all commands stored in the history</li>
    <li><code>last</code>: shows the most recent command</li>
    <li><code>id</code>: lists the available history through the common interface</li>
  </ul>

  <p>If no argument is provided, the script displays the usage message.</p>

  <h2>Example</h2>

  <pre><code>python histopy.py listall</code></pre>

  <h2>Notes</h2>

  <p>This project is designed to be simple and maintainable. It can be expanded to support more shells and terminal types, such as Bash, Zsh, Fish, PowerShell, and others.</p>