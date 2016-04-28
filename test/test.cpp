#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <cpprest/http_client.h>
#include <cpprest/http_listener.h>



void handle_get(web::http::http_request request)
{
    ucout << request.to_string() << std::endl;
    request.reply(web::http::status_codes::OK);
}



int main(int argc, char* argv[])
{
    utility::string_t port = std::to_string(rand() % 10000 + 50000);
    utility::string_t address = U("http://localhost:");
    address.append(port);

    web::http::experimental::listener::http_listener listener(address);
    try {
        listener.open().wait();
    } catch (const std::exception &e) {
        printf("Error exception:%s\n", e.what());
        return 0;
    }
    listener.support(web::http::methods::GET, handle_get);

    // Create http_client to send the request.
    web::http::client::http_client client(address);

    // Build request URI and start the request.
    web::http::uri_builder builder(U("/"));
    builder.append_query(U("q"), U("Casablanca Test"));
    pplx::task<web::http::http_response> requestTask = client.request(
        web::http::methods::GET,
        builder.to_string());

    // Handle response headers arriving.
    requestTask.then([=](web::http::http_response response)
    {
        printf("Received response status code:%u\n", response.status_code());
    });

    // Wait for all the outstanding I/O to complete and handle any exceptions
    try {
        requestTask.wait();
        listener.close().wait();
    } catch (const std::exception &e) {
        printf("Error exception:%s\n", e.what());
    }

    return 0;
}
