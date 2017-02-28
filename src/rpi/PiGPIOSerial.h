

#ifndef PIGPIOSERIAL_H
#define PIGPIOSERIAL_H

#include <IPlatformSerial.h>
#include <stdint.h>

class PiGPIOSerial : public IPlatformSerial
{
 public:
    PiGPIOSerial(int clk_pin, int dat_pin);

    int init();
    void send(unsigned char *buf, size_t len);

    int iface_num;

    ~PiGPIOSerial();

 private:
    volatile unsigned *gpio;
    volatile unsigned *gpio_set;
    volatile unsigned *gpio_clr;

    int fd;
    uint32_t dat_mask;
    uint32_t clk_mask;
    uint8_t m_dat_pin;
    uint8_t m_clk_pin;
    
};

#endif /* PIGPIOSERIAL_H */
