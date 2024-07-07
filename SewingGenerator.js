import React, { useState, useRef } from 'react';

const SVGPatternGenerator = () => {
  const [svgContent, setSvgContent] = useState('');
  const [scale, setScale] = useState(1);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const fileInputRef = useRef(null);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setSvgContent(e.target.result);
      };
      reader.readAsText(file);
    }
  };

  const handleScaleChange = (event) => {
    setScale(parseFloat(event.target.value));
  };

  const handlePositionChange = (axis, value) => {
    setPosition(prev => ({ ...prev, [axis]: parseInt(value) }));
  };

  const generateModifiedSVG = () => {
    if (!svgContent) return '';

    const parser = new DOMParser();
    const svgDoc = parser.parseFromString(svgContent, 'image/svg+xml');
    const svgElement = svgDoc.documentElement;

    // Apply transformations
    svgElement.setAttribute('transform', `translate(${position.x},${position.y}) scale(${scale})`);

    // Get the modified SVG as a string
    const serializer = new XMLSerializer();
    return serializer.serializeToString(svgDoc);
  };

  const exportSVG = () => {
    const modifiedSVG = generateModifiedSVG();
    const blob = new Blob([modifiedSVG], { type: 'image/svg+xml' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = 'modified_sewing_pattern.svg';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div style={{ padding: '1rem' }}>
      <h1 style={{ fontSize: '1.5rem', fontWeight: 'bold', marginBottom: '1rem' }}>SVG Sewing Pattern Generator</h1>
      <input 
        type="file" 
        accept=".svg" 
        onChange={handleFileUpload} 
        ref={fileInputRef}
        style={{ marginBottom: '1rem', display: 'block' }}
      />
      {svgContent && (
        <div>
          <div style={{ marginBottom: '1rem' }}>
            <label>Scale: </label>
            <input 
              type="number" 
              value={scale} 
              onChange={handleScaleChange} 
              step="0.1"
              min="0.1"
              style={{ marginLeft: '0.5rem' }}
            />
          </div>
          <div style={{ marginBottom: '1rem' }}>
            <label>Position X: </label>
            <input 
              type="number" 
              value={position.x} 
              onChange={(e) => handlePositionChange('x', e.target.value)}
              style={{ marginLeft: '0.5rem', marginRight: '1rem' }}
            />
            <label>Y: </label>
            <input 
              type="number" 
              value={position.y} 
              onChange={(e) => handlePositionChange('y', e.target.value)}
              style={{ marginLeft: '0.5rem' }}
            />
          </div>
          <button 
            onClick={exportSVG}
            style={{ marginBottom: '1rem', padding: '0.5rem', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer' }}
          >
            Export Modified SVG
          </button>
          <div style={{ border: '1px solid #ccc', padding: '1rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>Preview</h2>
            <div dangerouslySetInnerHTML={{ __html: generateModifiedSVG() }} />
          </div>
        </div>
      )}
    </div>
  );
};

export default SVGPatternGenerator;