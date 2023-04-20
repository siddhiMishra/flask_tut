
 const url_all = 'http://10.226.53.230:5000'

function getallproducts() {
  // const url = 'http://10.226.53.230:5000/allproducts'
  const url = url_all + '/allproducts'
  fetch(url).then(response => response.json())
    .then(data => {
      const products = data.products
      console.log(products)
      const content = document.getElementById("content")
      let list = products.map(pr => {
        return `<li>name: ${pr.name}</li>`
      })
      content.innerHTML = `<ul>${list.join(' ')}</ul>`
    }
    )

}


// console.log(data)

function getOuput() {
  const inp = document.getElementById("inp");
  
const outp = document.getElementById("outp");
  fetch( url_all + '/allproducts').then(response => response.json())
    .then(data => {
      const products = data.products;
      const product = products.find(p => p.name == inp.value);
      if (product) {

        outp.value = product.company;

      }
    });
}




function readfile() {
  
const outp = document.getElementById("outp");

  var fileInput = document.getElementById('myFileInput');


  var formData = new FormData();
  formData.append('siddhi', get);
console.log(formData)
  // Send FormData object to Flask server using fetch
  fetch( url_all + '/reverse', {
    method: 'POST',
    body: formData
  })
  
    .then(response => response.json())
    .then(data => {
      console.log(data.message);
      outp.value = data.message;
    })
    .catch(error => {
      console.error(error);
    });

}





function reverseString() {
  var inputString = document.getElementById('inp').value;
  fetch( url_all + '/reverse', {
      method: 'POST',
      body: JSON.stringify({input_string: inputString}),
      headers: {'Content-Type': 'application/json'}
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('result').value = data.message ;
  })
  .catch(error => console.error(error));
}



