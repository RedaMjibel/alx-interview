#0x06. Star Wars API
<div class="d-flex flex-wrap">

<div class="flex-grow-1" id="curriculum_navigation_content">
      
<div class="project row">
  <div class="col-xs-12 col-lg-10 contains-images">

  <h1 class="gap">
  0x06. Star Wars API
    
  </h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:17,&quot;value&quot;:&quot;Algorithm&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:36,&quot;value&quot;:&quot;API&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:46,&quot;value&quot;:&quot;JavaScript&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"></div>

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;weight&quot;:1,&quot;correction&quot;:{&quot;released&quot;:true,&quot;auto_correction_available_at&quot;:&quot;2024-04-16T06:00:00.000+03:00&quot;,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:false},&quot;bpi&quot;:{&quot;current&quot;:true,&quot;started&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2024-04-15T06:00:00.000+03:00&quot;,&quot;ends_at&quot;:&quot;2024-04-19T06:00:00.000+03:00&quot;,&quot;second_deadline_at&quot;:&quot;2024-04-22T06:00:00.000+03:00&quot;}}}" data-react-cache-id="projects/ProjectMetadata-0"></div>




    


<div id="project_id" style="display: none" data-project-id="1219"></div>



      

      

  <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p>The &ldquo;0. Star Wars Characters&rdquo; project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.</p>

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>HTTP Requests in JavaScript</strong>:</p>

<ul>
<li>Understanding how to make HTTP requests to external services using the <code>request</code> module or alternatives like <code>fetch</code> in Node.js.</li>
<li><a href="/rltoken/iRse23lnV4gAsD9JJTJMMQ" title="A Complete Guide to Making HTTP Requests in Node.js" target="_blank">A Complete Guide to Making HTTP Requests in Node.js</a></li>
</ul></li>
<li><p><strong>Working with APIs</strong>:</p>

<ul>
<li>Understanding the basics of RESTful APIs and how to interact with them.</li>
<li>Parsing JSON data returned by APIs.</li>
<li><a href="/rltoken/KyGS_uB68mLaP5irrH8JVA" title="Working with APIs in JavaScript" target="_blank">Working with APIs in JavaScript</a></li>
</ul></li>
<li><p><strong>Asynchronous Programming</strong>:</p>

<ul>
<li>Managing asynchronous operations with callbacks, promises, and async/await syntax.</li>
<li>Handling API response data asynchronously.</li>
<li><a href="/rltoken/tdKMGJrRstCkXSReNfRFpQ" title="Asynchronous Programming in JavaScript" target="_blank">Asynchronous Programming in JavaScript</a></li>
</ul></li>
<li><p><strong>Command Line Arguments in Node.js</strong>:</p>

<ul>
<li>Using the <code>process.argv</code> array to access command-line arguments passed to a Node.js script.</li>
<li><a href="/rltoken/oWBOWJZLF_D9GfOydPz6Kg" title="How to Parse Command Line Arguments in Node.js" target="_blank">How to Parse Command Line Arguments in Node.js</a></li>
</ul></li>
<li><p><strong>Array Manipulation and Iteration</strong>:</p>

<ul>
<li>Iterating over arrays and manipulating data structures to format and display character names.</li>
<li><a href="/rltoken/8zdG036OYYvVco_AZTExoA" title="JavaScript Array Methods" target="_blank">JavaScript Array Methods</a></li>
</ul></li>
</ol>

<p>By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.</p>

<h2>Additional Resources</h2>

<ul>
<li><a href="/rltoken/du6hlPQm6qi4A7eEursNhQ" title="Mock Technical Interview" target="_blank">Mock Technical Interview</a></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS using <code>node</code> (version 10.14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a href="/rltoken/9P3gH5mVdJCEKL87E-IMaA" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="/rltoken/WjMvQfBMKBdsNUuHyg55Dw" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="/rltoken/Xp81RT-Sfi7uE_kNCSXunw" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>
