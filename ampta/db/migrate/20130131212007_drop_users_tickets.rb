class DropUsersTickets < ActiveRecord::Migration
  def up
    drop_table :users_tickets
  end

  def down
    create_table :users_tickets do |t|
    end
  end
end
