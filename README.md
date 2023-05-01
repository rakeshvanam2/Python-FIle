# Python-FIle

The microservice defines a single endpoint '/word-frequency' that expects a POST request with a JSON payload containing a 'url' field specifying the URL of the web page to be processed.

When a request is received, the microservice retrieves the HTML content of the page using the requests library and parses the content using the BeautifulSoup library to extract all the text from the page. It then splits the text into words, converts them to lowercase and removes any non-alphabetic characters. The frequency of each unique word is then counted using the Counter class from the collections library.

Finally, the resulting frequency counts are converted to a dictionary and serialized to JSON using the json library. The JSON response is returned to the client with a 200 status code and a 'Content-Type' header indicating that the response is JSON.

send a POST request to http://localhost:5000/words with a JSON payload containing the URL of the website you want to analyze:

curl -X POST -H "Content-Type: application/json" -d '{"url": "http://example.com"}' http://localhost:5000/words
