document.addEventListener("DOMContentLoaded", function() {
    const preGateToggle = document.getElementById('pre-gate-toggle');
    const postGateToggle = document.getElementById('post-gate-toggle');
    const sharedGateToggle = document.getElementById('shared-gate-toggle');
    const encoderToggle = document.getElementById('encoder-toggle');
    const extruderToggle = document.getElementById('extruder-toggle');
    const toolheadToggle = document.getElementById('toolhead-toggle');
    
    // Add event listeners to all checkboxes to toggle visibility
    preGateToggle.addEventListener('change', function() {
        document.getElementById('pre-gate').style.display = preGateToggle.checked ? 'block' : 'none';
    });
    
    postGateToggle.addEventListener('change', function() {
        document.getElementById('post-gate').style.display = postGateToggle.checked ? 'block' : 'none';
    });
    
    sharedGateToggle.addEventListener('change', function() {
        document.getElementById('shared-gate').style.display = sharedGateToggle.checked ? 'block' : 'none';
    });
    
    encoderToggle.addEventListener('change', function() {
        document.getElementById('encoder').style.display = encoderToggle.checked ? 'block' : 'none';
    });
    
    extruderToggle.addEventListener('change', function() {
        document.getElementById('extruder').style.display = extruderToggle.checked ? 'block' : 'none';
    });
    
    toolheadToggle.addEventListener('change', function() {
        document.getElementById('toolhead').style.display = toolheadToggle.checked ? 'block' : 'none';
    });
});