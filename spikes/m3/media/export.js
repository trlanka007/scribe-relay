// Generate a local PNG from the existing trusted synthetic SVG in a browser.
const button = document.querySelector('#export');
const status = document.querySelector('#status');
button.addEventListener('click', async () => {
  button.disabled = true;
  try {
    const image = document.querySelector('#fixture');
    await image.decode();
    const canvas = document.createElement('canvas');
    canvas.width = 480;
    canvas.height = 240;
    canvas.getContext('2d').drawImage(image, 0, 0, 480, 240);
    const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/png'));
    if (!blob) throw new Error('PNG export unavailable');
    const bytes = await blob.arrayBuffer();
    const digest = await crypto.subtle.digest('SHA-256', bytes);
    const hash = Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2, '0')).join('');
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'anchor.png';
    link.textContent = 'Save anchor.png';
    const old = document.querySelector('#download a');
    if (old) URL.revokeObjectURL(old.href);
    document.querySelector('#download').replaceChildren(link);
    status.textContent = 'PNG 480 × 240; SHA-256: ' + hash + '; bytes: ' + blob.size;
  } catch (error) {
    status.textContent = 'Export failed: ' + error.message + '. Use the localhost instructions.';
  } finally {
    button.disabled = false;
  }
});
