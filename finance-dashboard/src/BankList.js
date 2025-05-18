import React, { useEffect, useState } from "react";
import { getBanks } from "./api"; // Or from BankService.js

const BankList = () => {
  const [banks, setBanks] = useState([]);

  useEffect(() => {
    const fetchBanks = async () => {
      const data = await getBanks();
      setBanks(data);
    };

    fetchBanks();
  }, []);

  return (
    <div>
      <h2>Banks & Interest Rates</h2>
      <ul>
        {banks.map((bank) => (
          <li key={bank.id}>
            <strong>{bank.name}</strong><br />
            FD Interest: {bank.fd_interest}%<br />
            RD Interest: {bank.rd_interest}%<br />
            Savings Interest: {bank.savings_interest}%
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BankList;