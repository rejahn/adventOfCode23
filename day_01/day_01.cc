#include <iostream>
#include <string>
#include <list>
#include <fstream>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " <filename>\n";
        return 1;
    }

    std::ifstream input(argv[1]);
    if (!input.is_open()) {
        std::cout << "Failed to open file." << std::endl;
        return 1;
    }

    std::string buffer;
    std::list<std::string> calibration;
    while (std::getline(input, buffer)) {
        std::string digits;
        for (char ch : buffer) {
            if (std::isdigit(ch)) {
                digits.push_back(ch);
            }
        }
        if (!digits.empty()) {
            if (digits.size() == 1) {
                // Duplicate the digit
                digits += digits;
            } else if (digits.size() >= 3) {
                // Keep only the first and last digit
                digits = digits.front() + std::string(1, digits.back());
            }
            // If the size is 2, keep it as is
            calibration.push_back(digits);
        }
    }

    int sum = 0;
    for (const auto& numStr : calibration) {
        sum += std::stoi(numStr);
    }

    std::cout << "Sum: " << sum << std::endl;
    return 0;
}